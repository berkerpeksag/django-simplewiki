from django.conf.urls import patterns, url
from django.views.generic.base import RedirectView

from .settings import MAIN_PAGE_SLUG
from .views import DocumentDetail, DocumentRevision

urlpatterns = patterns('simplewiki.views',
    url(r'^$', RedirectView.as_view(url=MAIN_PAGE_SLUG, permanent=True)),
    url(r'^(?P<slug>[a-z0-9-]+)$', DocumentDetail.as_view(), name='document_detail'),
    url(r'^(?P<slug>[a-z0-9-]+)/edit/$', DocumentRevision.as_view(), name='document_update'),
)
