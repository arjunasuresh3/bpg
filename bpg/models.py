from django.db import models

# Create your models here.
class Area(models.Model):
    area_name = models.CharField(max_length=200)

class Pglist(models.Model):
    area = models.ForeignKey(Area)
    pname = models.CharField(max_length=200)
    paddress = models.CharField(max_length=1000)    
    phone = models.CharField(max_length=200)
    prdes = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.pname
    
