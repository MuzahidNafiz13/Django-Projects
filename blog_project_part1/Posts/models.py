from django.db import models
from Categories.models import Category
from django.contrib.auth.models import User


# Create your models here.
class Posts(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(default=None)
    category=models.ManyToManyField(Category)
    author=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title