
from django.conf.urls import include, url
from django.contrib import admin
from django_project.views import home,about,contact,privacy,sitemap,google
from django.conf.urls import patterns, url
from blog import views,urls
from blog.models import blog,comment


urlpatterns = patterns(
    url(r'^$', home , name='index'),
    url(r'^sitemap.xml/', sitemap , name='sitemap'),
    url(r'^googlefa975541a78f7cc0.html/', google , name='google'),
    url(r'^about-team-spotable/', about , name='about'),
    url(r'^contact-spotable/', contact , name='contact'),
    url(r'^pricavy-policy-of-spotable/', privacy , name='privacy'),
    url(r'^blog/', include('blog.urls', namespace="blog")),
    url(r'^admin/', include(admin.site.urls)),


)
