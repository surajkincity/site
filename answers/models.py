from django.db import models
from django.forms import ModelForm
import datetime


class blog(models.Model):
    title = models.CharField(max_length=5000)
    body = models.TextField()
    date = models.DateField(default = datetime.datetime.now())
    def slug(self):
        slugit= self.title.replace(' ', '-').replace('?', '_').replace('@', '*')
        return slugit




class comment(models.Model):
    blog = models.CharField(max_length=5000,null=True,blank=True)
    comment = models.TextField()
    date = models.DateField(default = datetime.datetime.now())
