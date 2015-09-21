from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login',
     {'template_name': 'registration/login.html',
      'extra_context': {'next': '/wiki'}}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
     {'next_page': '/wiki'}),

    url(r'^wiki/', include('simplewiki.urls')),

    url(r'^$', TemplateView.as_view(template_name='testproject/index.html')),
]
