from django import forms

from .models import newsletter,leads,contact

class contactform(forms.ModelForm):
    class Meta:
        model = contact
        fields = ('message','email')

class leadsform(forms.ModelForm):
    class Meta:
        model = leads
        fields = ('website','email')

class newsletterform(forms.ModelForm):
    class Meta:
        model = newsletter
        fields = ('email')
