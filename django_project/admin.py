from django.contrib import admin

# Register your models here.

from .models import leads,newsletter,contact


admin.site.register(leads)
admin.site.register(newsletter)
admin.site.register(contact)
