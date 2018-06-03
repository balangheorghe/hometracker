from django.db import models

# Create your models here.
class Location(models.Model):
    username = models.CharField(max_length=50)
    lat = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)
    timestamp = models.DateTimeField()
