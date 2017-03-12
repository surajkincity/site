from django.shortcuts import render
from django.shortcuts import get_object_or_404, render , redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import blog,comment
from django.template import Context, Template
import datetime
from datetime import date,timedelta
from django import forms
from django.utils import timezone
from .forms import blogform,comentform


def blogindex(request):
    blogs = blog.objects.all()
    date = datetime.datetime.now().date()
    return render(request, 'blog/index.html',
                  {'date': date,
                  'blogs':blogs

                  })

def new(request):
    date = datetime.datetime.now().date()
    blogs = blog.objects.all()
    if request.method == "POST":
        form = blogform(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'blog/index.html',
                          {'date': date,
                          'blogs':blogs
                          })
    else:
        form = blogform()
        return render(request, 'blog/new.html',
                      {'date': date,
                      'blogs':blogs,
                      'form' : form
                      })
