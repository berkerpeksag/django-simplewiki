from django.conf.urls import url

from .views import (
    DocumentIndex, DocumentCreate, DocumentDetail, DocumentUpdate,
    RevisionList, RevisionDetail,
)

urlpatterns = [
    url(r'^$', DocumentIndex.as_view(), name='simplewiki.index'),
    url(r'^create/$', DocumentCreate.as_view(), name='simplewiki.create'),
    url(r'^(?P<slug>[a-z0-9-]+)/$',
        DocumentDetail.as_view(), name='simplewiki.detail'),
    url(r'^(?P<slug>[a-z0-9-]+)/edit/$',
        DocumentUpdate.as_view(), name='simplewiki.update'),
    url(r'^(?P<slug>[a-z0-9-]+)/revisions/$',
        RevisionList.as_view(), name='simplewiki.revisions'),
    url(r'^(?P<slug>[a-z0-9-]+)/revision/(?P<pk>[0-9]+)/$',
        RevisionDetail.as_view(), name='simplewiki.revision'),
]
