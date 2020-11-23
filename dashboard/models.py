from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation




# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=200, verbose_name='category')

    def __str__(self):
        return self.name


class Product(models.Model):
    category          = models.ForeignKey(ProductCategory, on_delete= models.CASCADE, related_name='category', blank=False, null=True)
    image             = models.ImageField(upload_to='products/')
    name              = models.CharField(max_length=200, unique=True)
    slug              = models.SlugField(max_length=200, unique=True)
    price             = models.DecimalField(max_digits=10, decimal_places=2)
    created_on        = models.DateTimeField(default=timezone.now)
    description       = models.TextField(blank=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')
    

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name











