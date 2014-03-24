from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='base.html')),

    # Example:
    # url(r'^company/', include('procompanyject.foo.urls')),

    # django multiuploader
    # https://github.com/xacce/django_ffiler
    url(r'^design/', include('apps.django_ffiler.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
