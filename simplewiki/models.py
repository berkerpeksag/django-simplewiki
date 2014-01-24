from __future__ import print_function, unicode_literals

from django.conf import settings
from django.db import models
from django.utils.encoding import smart_unicode
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify

from markdown import markdown

from .managers import DocumentManager


USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

MARKUPS = (
    ('rst', 'reStructuredText'),
    ('md', 'Markdown'),
)


class Document(models.Model):

    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=100, unique=True)

    is_published = models.BooleanField(_('Publish?'), default=True)
    markup = models.CharField(max_length=3, choices=MARKUPS, default='md')

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    objects = DocumentManager()

    class Meta:
        verbose_name = _('Document')
        verbose_name_plural = _('Documents')
        ordering = ('-updated_on',)

    def save(self, *args, **kwargs):
        slug = slugify(self.title)
        if self.slug != slug:
            self.slug = slug

        super(Document, self).save(*args, **kwargs)

    @property
    def current_revision(self):
        # TODO: Probably inefficient
        return Revision.objects.filter(document=self).latest('created_on')

    @property
    def get_contributors(self):
        # TODO: Highly inefficient
        queryset = Revision.objects.filter(document=self)
        contributors = set([r.creator for r in queryset])
        return contributors

    @models.permalink
    def get_absolute_url(self):
        return 'simplewiki.detail', (), {'slug': self.slug}

    def __unicode__(self):
        return smart_unicode(self.title)


class Revision(models.Model):

    document = models.ForeignKey(Document, related_name='revisions')

    summary = models.CharField(max_length=100, blank=True)

    content = models.TextField(_('Content'))
    rendered = models.TextField(blank=True)  # HTML version of the content

    created_on = models.DateTimeField(auto_now_add=True)

    creator = models.ForeignKey(USER_MODEL, blank=True)

    class Meta:
        ordering = ('-created_on',)

    def save(self, *args, **kwargs):
        if self.document.markup == 'md':
            self.rendered = markdown(self.content)
        else:
            self.rendered = self.content

        super(Revision, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return 'simplewiki.detail', (), {'slug': self.document.slug}

    def __unicode__(self):
        args = self.document.title, self.content[:50]
        return smart_unicode('%s: %s' % args)
