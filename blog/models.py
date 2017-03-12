from django.db import models
from django.forms import ModelForm
import datetime


class blog(models.Model):
    title = models.CharField(max_length=5000)
    body = models.TextField()
    date = models.DateField(default = datetime.datetime.now())



class comment(models.Model):
    blog = models.ForeignKey(blog, on_delete=models.CASCADE,null=True,blank=True)
    comment = models.TextField()
    date = models.DateField(default = datetime.datetime.now())
