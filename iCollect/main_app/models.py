from django.db import models

# Create your models here.

class Collection(models.Model):
    year = models.IntegerField()
    name = models.CharField(max_length = 100)
    type = models.CharField(max_length = 100)
    price = models.IntegerField()
    condition = models.CharField(max_length = 100)
    description = models.TextField(max_length=250)
    
    
    
