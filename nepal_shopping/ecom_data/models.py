from django.db import models
from django.contrib.postgres.fields import JSONField
from datetime import date
from django.utils import timezone

class Ecomweb(models.Model):
    name = models.CharField(max_length=128)
    country = models.CharField(max_length=128)
    website = models.CharField(max_length=128)

class Searchquery(models.Model):
    name = models.CharField(max_length=128)
    date = models.DateTimeField(default=timezone.now,blank=True)
    search_type = models.CharField(max_length=128)