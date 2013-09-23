from __future__ import print_function, unicode_literals

from django.conf import settings
from django.conf.urls import patterns, url
from django.views.generic.base import RedirectView

from .settings import MAIN_PAGE_SLUG
from .views import DocumentDetail, DocumentRevision

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url=MAIN_PAGE_SLUG, permanent=not settings.DEBUG), name='simplewiki.index'),
    url(r'^(?P<slug>[a-z0-9-]+)/$', DocumentDetail.as_view(), name='simplewiki.detail'),
    url(r'^(?P<slug>[a-z0-9-]+)/edit/$', DocumentRevision.as_view(), name='simplewiki.update'),
)
