
from django.db import models

# Create your models here.
class Actor(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    dp = models.CharField(max_length=512, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)

