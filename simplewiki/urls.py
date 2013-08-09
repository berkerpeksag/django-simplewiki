from django.conf.urls import patterns, url

from .views import DocumentDetailView, IndexView

urlpatterns = patterns('simplewiki.views',
    url(r'^$', IndexView.as_view()),
    url(r'^(?P<slug>[a-z0-9-]+)$', DocumentDetailView.as_view(), name='document_detail'),
)
