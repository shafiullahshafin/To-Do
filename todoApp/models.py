from django.db import models
import datetime

# Create your models here.

class TodoData(models.Model):
    title=models.CharField(max_length=30)
    desc=models.CharField(max_length=200)
    created=models.DateField()
    dueDate=models.DateField()
    isCompleted=models.BooleanField()


    def __str__(self):
        return self.title
