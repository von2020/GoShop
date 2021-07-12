from django.db import models
from django.utils import timezone
from dashboard.models import Product

# Create your models here.

class SalesReport(models.Model):
    product      = models.ForeignKey(Product, on_delete= models.CASCADE, related_name='product_name', blank=False, null=True)
    amount    = models.DecimalField(max_digits=10, decimal_places=2)
    date      = models.DateTimeField(default=timezone.now)
    
    

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name