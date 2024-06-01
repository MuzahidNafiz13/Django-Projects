from django.db import models

# Create your models here.

class Student(models.Model):
    name= models.CharField(max_length=50)
    roll=models.IntegerField()
    address=models.TextField()
    father_name=models.CharField(default="Nafiz", max_length=50)

    def __str__(self):
        return f"Roll: {self.roll}, Name:{self.name}"
