from django.db import models

# Create your models here.
class Books(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    rating = models.CharField(max_length=30)
    reviews = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    year = models.CharField(max_length=30)
    genre = models.CharField(max_length=30)