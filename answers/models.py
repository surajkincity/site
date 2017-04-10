from django.db import models
from django.forms import ModelForm
import datetime


class blog(models.Model):
    title = models.CharField(max_length=5000)
    body = models.TextField()
    date = models.DateField(default = datetime.datetime.now())
    name = models.CharField(max_length=5000)
    def slug(self):
        slugit= self.title.replace(' ', '-').replace('?', '').replace('@', '*')
        return slugit
    def ic(self):
        icit = self.name[0]
        return icit




class comment(models.Model):
    name = models.CharField(max_length=5000)
    blog = models.CharField(max_length=5000,null=True,blank=True)
    comment = models.TextField()
    date = models.DateField(default = datetime.datetime.now(),blank=True)

    def ic(self):
        icit = self.name[0]
        return icit
