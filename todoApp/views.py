from django.shortcuts import render,redirect,HttpResponse
from .models import TodoData
from django.urls import reverse
from .forms import TodoDataForm

# Create your views here.


def home(request):
    tasks = TodoData.objects.all()
    completed_tasks = tasks.filter(isCompleted=True)  
    incompleted_tasks = tasks.filter(isCompleted=False)  

    query=""
    if request.method=="POST":
        query = request.POST.get('query')

    filtered=[]
    for task in tasks:
        if (query.lower() in task.title.lower()) and not(query==""):
            filtered.append(task)

    contexts={
        "completed_tasks":completed_tasks,
        "incompleted_tasks":incompleted_tasks,
        "filtered":filtered
    }
    return render(request,"home.html",contexts)

def dummy(request):
    return HttpResponse('{"name":"dummy","age":29, "city":"raj"}')



    
def addTask(request):
    if(request.method=="POST"):
        form=TodoDataForm(request.POST)
        form.save()
        return redirect("home")
    else:
        form=TodoDataForm()
        return render(request,"addTask.html",{"form":form})
    

def edit(request,id):
    task=TodoData.objects.get(id=id)
    contexts={
        "task": task
    }
    return render(request,"edit.html",contexts)

def saveEdit(request,id):
    todoData=TodoData.objects.get(id=id)
    if request.method=="POST":
        todoData.title = request.POST.get('title')
        todoData.desc = request.POST.get('desc')
        todoData.created = request.POST.get('created')
        todoData.dueDate = request.POST.get('dueDate')
        if(request.POST.get('isCompleted')=="on"):
            todoData.isCompleted=True
        else:
            todoData.isCompleted=False
        todoData.save()
        return redirect(reverse("description",args=[id]))
    return redirect('home')


def description(request,id):
        task=TodoData.objects.get(id=id)
        return render(request, 'description.html', {'task': task})

def update_status(request,id):
        task=TodoData.objects.get(id=id)
        task.isCompleted=not task.isCompleted
        task.save()
        return render(request, 'description.html', {'task': task})

def update_home(request,id):
        task=TodoData.objects.get(id=id)
        task.isCompleted=not task.isCompleted
        task.save()
        return redirect('home')

def delete(request,id):
        task=TodoData.objects.get(id=id)
        task.isCompleted=not task.isCompleted
        task.delete()
        return redirect('home')

