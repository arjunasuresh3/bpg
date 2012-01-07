from django.db import models

# Create your models here.
class Area(models.Model):
    area_name = models.CharField(max_length=200)

class Pglist(models.Model):
    area_id = models.ForeignKey(Area)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()
