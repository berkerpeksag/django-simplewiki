from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),

    (r'^accounts/login/$', 'django.contrib.auth.views.login',
     {'template_name': 'registration/login.html',
      'extra_context': {'next': '/wiki'}}),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout',
     {'next_page': '/wiki'}),

    url(r'^wiki/', include('simplewiki.urls')),
)
