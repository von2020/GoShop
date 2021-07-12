from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Message(models.Model):
    message        = models.TextField(blank=True)
    name           = models.CharField(max_length=200, unique=True)
    email          = models.EmailField(verbose_name='email address',max_length=255,unique=True,default='')
    date_sent      = models.DateTimeField(auto_now_add=True)
    
    

    class Meta:
        ordering = ['-date_sent']

    def __str__(self):
        return self.name