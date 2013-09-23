from __future__ import print_function, unicode_literals

from django.conf import settings

WIKI_TEXT_FORMAT = getattr(settings, 'WIKI_TEXT_FORMAT', 'reST')
MAIN_PAGE_SLUG = getattr(settings, 'MAIN_PAGE_SLUG', 'main-page')
