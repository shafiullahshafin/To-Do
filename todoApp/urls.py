from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("addTask/", views.addTask, name="addTask"),
    path('description/<int:id>/', views.description, name='description'),
    path('update_status/<int:id>/', views.update_status, name='update_status'),
    path('update_home/<int:id>/', views.update_home, name='update_home'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('saveEdit/<int:id>/', views.saveEdit, name='saveEdit'),  
    path('dummy/', views.dummy, name='dummy')
]