from django.db import models


# Create your models here.
class Location(models.Model):
    username = models.CharField(max_length=50)
    lat = models.FloatField()
    lng = models.FloatField()
    timestamp = models.DateTimeField()


class LastLocation(models.Model):
    username = models.CharField(max_length=50)
    lat = models.FloatField()
    lng = models.FloatField()
    timestamp = models.FloatField()