from django.db import models
from Categories.models import Category
from Author.models import Author

# Create your models here.
class Posts(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(default=None)
    category=models.ManyToManyField(Category)
    author=models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title