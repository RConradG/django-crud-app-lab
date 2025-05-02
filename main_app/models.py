from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.name

class Collection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='collections')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('collection-detail', kwargs={'collection_id': self.id})

class Item(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='item')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    purchase_date = models.DateField(null=True, blank=True)
    estimated_value = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-estimated_value']
    