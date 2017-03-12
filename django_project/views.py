from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html', )

def about(request):
    return render(request, 'about.html', )

def contact(request):
    return render(request, 'contact.html', )

def privacy(request):
    return render(request, 'privacy.html', )

def sitemap(request):
    return render(request, 'sitemap.xml')

def google(request):
    return render(request, 'googlefa975541a78f7cc0.html')
