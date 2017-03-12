from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.blogindex, name='blogindex'),
    url(r'^new/$', views.new, name='new'),
    url(r'^(?P<pk>\d+)/edit/$', views.edit, name='edit'),
    url(r'^(?P<slug>[\w-]+)/$', views.show, name='show'),

]
