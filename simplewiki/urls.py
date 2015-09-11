from django.conf.urls import url

from .views import (DocumentIndex, DocumentCreate, DocumentDetail,
                    DocumentAddRevision)

urlpatterns = [
    url(r'^$', DocumentIndex.as_view(), name='simplewiki.index'),
    url(r'^create/$', DocumentCreate.as_view(), name='simplewiki.create'),
    url(r'^(?P<slug>[a-z0-9-]+)/$',
        DocumentDetail.as_view(), name='simplewiki.detail'),
    url(r'^(?P<slug>[a-z0-9-]+)/edit/$',
        DocumentAddRevision.as_view(), name='simplewiki.update'),
]
