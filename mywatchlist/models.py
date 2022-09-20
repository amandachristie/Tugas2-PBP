from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class MyWatchList(models.Model):
    watched = models.BooleanField()
    title = models.TextField()
    rating = models.IntegerField()
    release_date = models.DateField()
    review = models.TextField()