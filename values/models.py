from django.db import models
from django.utils import timezone
import time
# Create your models here.


class api(models.Model):
    temperature = models.CharField(max_length=1000, default='0')
    humidity = models.CharField(max_length=1000, default='0')
    time = models.TimeField(blank=True, null=True)
    moisture = models.CharField(max_length=1000,default ='0')
    distance = models.CharField(max_length=1000,default='0')


    def __str__(self):
        return self.temperature
