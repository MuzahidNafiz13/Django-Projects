from django.db import models
from Author.models import Author 

# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=50)
    about=models.TextField(max_length=255, blank=True, null=True)
    author=models.OneToOneField(Author, on_delete=models.CASCADE,default=None)

    def __str__(self) -> str:
        return self.name