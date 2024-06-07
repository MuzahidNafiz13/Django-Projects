from django.db import models
from Categories.models import Category
from django.contrib.auth.models import User


# Create your models here.
class Posts(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(default=None)
    category=models.ManyToManyField(Category)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    image= models.ImageField(upload_to='uploads/', blank=True, null=True)
    def __str__(self) -> str:
        return self.title
    
class Comment(models.Model):
    post=models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comments')
    name=models.CharField(max_length=30)
    email= models.EmailField(max_length=254)
    body=models.TextField()
    created_on= models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return f"Comments By {self.name}"