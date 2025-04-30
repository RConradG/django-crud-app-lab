from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.name

class Collection(models.Model):
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.Charfield(max_length=100)
    description = models.TextField(blank=True)
    purchase_date = models.DateField(null=True, blank=True)
    estimated_value = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name
    