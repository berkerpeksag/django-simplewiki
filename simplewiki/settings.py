from django.conf import settings

WIKI_TEXT_FORMAT = getattr(settings, 'WIKI_TEXT_FORMAT', 'reST')
