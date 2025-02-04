from django import forms
from .models import TodoData

class TodoDataForm(forms.ModelForm):
    class Meta:
        model = TodoData
        fields = ['title', 'desc', 'created', 'dueDate', 'isCompleted']
        widgets = {
            'created': forms.DateInput(attrs={'type': 'date'}),
            'dueDate': forms.DateInput(attrs={'type': 'date'}),
        }
