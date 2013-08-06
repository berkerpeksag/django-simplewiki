from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from .views import DocumentDetailView

urlpatterns = patterns('simplewiki.views',
    url(r'^$', TemplateView.as_view(template_name="simplewiki/index.html"),
        name="index"),
    url(r'^(?P<slug>[a-z0-9-]+)$', DocumentDetailView.as_view()),
)
