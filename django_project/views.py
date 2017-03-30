from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import contactform,newsletterform,leadsform


def home(request):
    if request.method == "POST":
        form = leadsform(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            form = 'Thanks! We will get back to you shortly.'
            return render(request, 'index.html', {'form': form})
    else:
        form = leadsform()
        return render(request, 'index.html', {'form': form})


def about(request):
    return render(request, 'about.html', )

def contact(request):
    return render(request, 'contact.html',  )

def privacy(request):
    return render(request, 'privacy.html', )

def sitemap(request):
    return render(request, 'sitemap.xml')

def google(request):
    return render(request, 'googlefa975541a78f7cc0.html')
