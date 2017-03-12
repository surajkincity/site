from django.db import models
from django.forms import ModelForm
import datetime


class blog(models.Model):
    title = models.CharField(max_length=5000)
    body = models.TextField()
    date = models.DateField(default = django.utils.timezone.now())



class comment(models.Model):
    blog = models.CharField(max_length=5000)
    comment = models.TextField()
    date = models.DateField(default = django.utils.timezone.now())
