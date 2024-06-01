from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=255)
    bio=models.TextField(max_length=255)
    phone_no=models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
