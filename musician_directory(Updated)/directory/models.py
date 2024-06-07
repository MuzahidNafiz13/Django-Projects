from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    instrument_type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Album(models.Model):
    name = models.CharField(max_length=100)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE, related_name='albums')
    release_date = models.DateField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.name