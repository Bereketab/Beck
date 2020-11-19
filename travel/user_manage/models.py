from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.utils import timezone
from django.contrib.gis.db import models as m


class destination(models.Model,m.Model):
    name = models.CharField(max_length=30, unique=True)
    country = models.CharField( max_length=30, blank=True)
    description = models.CharField( max_length=150, blank=True) 
    coordinate = m.PointField()
    
    def __str__(self):
        return self.name
