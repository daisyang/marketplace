from django.conf.urls import patterns, include, url
from marketplace_app import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'marketplace.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$/', views.provider_index, name='provider_index'),
)
