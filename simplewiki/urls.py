from __future__ import print_function, unicode_literals

from django.conf import settings
from django.conf.urls import patterns, url

from .views import DocumentIndex, DocumentCreate, DocumentDetail, DocumentRevision

urlpatterns = patterns('',
    url(r'^$', DocumentIndex.as_view(), name='simplewiki.index'),
    url(r'^create/$', DocumentCreate.as_view(), name='simplewiki.create'),
    url(r'^(?P<slug>[a-z0-9-]+)/$', DocumentDetail.as_view(), name='simplewiki.detail'),
    url(r'^(?P<slug>[a-z0-9-]+)/edit/$', DocumentRevision.as_view(), name='simplewiki.update'),
)
