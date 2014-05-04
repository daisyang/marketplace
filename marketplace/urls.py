from django.conf.urls import patterns, include, url

from django.contrib import admin
from marketplace_app import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'marketplace.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.school_index, name='school_index'),   # this is default web page
    url(r'^provider/', include('marketplace_app.provider_urls', namespace='provider')),
    url(r'^school/', include('marketplace_app.school_urls', namespace='school')),
)
