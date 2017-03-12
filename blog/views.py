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

def show(request,slug):
    slug = slug.replace('-', ' ').replace('_', '?').replace('*', '@')
    post = get_object_or_404(blog, title=slug)
    date = datetime.datetime.now().date()
    comments = comment.objects.all()
    blogs = blog.objects.all()
    if request.method == "POST":
        form = comentform(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = comentform()
        return render(request, 'blog/detail.html',
                      {'date': date,
                      'post': post,
                      'form': form,
                      'comments':comments
                      })



def new(request):
    date = datetime.datetime.now().date()
    blogs = blog.objects.all()
    if request.method == "POST":
        form = blogform(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = blogform()
        return render(request, 'blog/new.html',
                      {'date': date,
                      'blogs':blogs,
                      'form' : form
                      })


def edit(request, pk):
    date = datetime.datetime.now().date()
    blogs = blog.objects.all()
    post = get_object_or_404(blog, pk=pk)
    if request.method == "POST":
        form = blogform(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = blogform()
    return render(request, 'blog/edit.html', {'form': form})
