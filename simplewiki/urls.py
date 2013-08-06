from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from .views import DocumentDetailView

urlpatterns = patterns('simplewiki.views',
    (r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^(?P<slug>[a-z0-9-]+)$', DocumentDetailView.as_view()),
)
