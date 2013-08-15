from django.conf.urls import patterns, url

from .views import DocumentDetail, DocumentRevision, DocumentIndex

urlpatterns = patterns('simplewiki.views',
    url(r'^$', DocumentIndex.as_view(), name='document_index'),
    url(r'^(?P<slug>[a-z0-9-]+)$', DocumentDetail.as_view(), name='document_detail'),
    url(r'^(?P<slug>[a-z0-9-]+)/edit/$', DocumentRevision.as_view(), name='document_update'),
)
