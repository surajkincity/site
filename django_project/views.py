from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import contactform,newsletterform,leadsform


def home(request):
	if request.method == "POST":
		form = leadsform(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			message = 'Thanks! We will get back to you shortly.'
			form = ' '
			display = 'none'
			return render(request, 'index.html', {'form': form, 'display' :display , 'message' :message})
		
	else:
		message = ''
		display = 'block'
		form = leadsform()
		return render(request, 'index.html', {'form': form, 'display' :display , 'message' :message})

def newsletter(request):
	if request.method == "POST":
		form = newsletterform(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			message = 'Suscribed'
			form = ' '
			display = 'none'
			return render(request, 'newsletter.html', {'form': form, 'display' :display , 'message' :message})
		
	else:
		message = ''
		display = 'inline-block'
		form = newsletterform()
		return render(request, 'newsletter.html', {'form': form, 'display' :display , 'message' :message})



def about(request):
	return render(request, 'about.html', )

def contact(request):
	if request.method == "POST":
		form = leadsform(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			message = 'Thanks! We will get back to you shortly.'
			form = ' '
			display = 'none'
			return render(request, 'contact.html', {'form': form, 'display' :display , 'message' :message})
		
	else:
		message = ''
		display = 'block'
		form = leadsform()
		return render(request, 'contact.html', {'form': form, 'display' :display , 'message' :message})

def privacy(request):
	return render(request, 'privacy.html', )

def sitemap(request):
	return render(request, 'sitemap.xml')

def google(request):
	return render(request, 'googlefa975541a78f7cc0.html')
