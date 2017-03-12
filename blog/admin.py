from django.contrib import admin

# Register your models here.

from .models import blog,comment


admin.site.register(blog)
admin.site.register(comment)
