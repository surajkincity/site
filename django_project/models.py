from django.db import models
from django.forms import ModelForm
import datetime


class contact(models.Model):
    email = models.CharField(max_length=5000)
    message = models.TextField()

class leads(models.Model):
    website = models.CharField(max_length=5000)
    email = models.CharField(max_length=5000)

class newsletter(models.Model):
    email = models.CharField(max_length=5000)


