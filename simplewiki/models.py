from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify

from markdown import markdown

from .managers import DocumentManager

USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class Document(models.Model):

    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=100, unique=True)

    is_published = models.BooleanField(_('Publish?'), default=True)

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

        super().save(*args, **kwargs)

    # TODO: Remove this
    @property
    def current_revision(self):
        # TODO: Probably inefficient
        return Revision.objects.filter(document=self).latest('created_on')

    @property
    def get_contributors(self):
        # TODO: Highly inefficient
        contributors = Revision.objects.filter(document=self)
        return ', '.join(set(str(c.creator) for c in contributors))

    @property
    def current(self):
        return self.revisions.latest()

    # TODO: Use @property?
    def rev(self, rev_id):
        return self.revisions.get(pk=rev_id)

    @models.permalink
    def get_absolute_url(self):
        return 'simplewiki.detail', (), {'slug': self.slug}

    def __str__(self):
        return self.title


class Revision(models.Model):

    document = models.ForeignKey(Document, related_name='revisions')

    summary = models.CharField(max_length=100, blank=True)

    content = models.TextField(_('Content'))
    rendered = models.TextField(blank=True)  # HTML version of the content

    created_on = models.DateTimeField(auto_now_add=True)

    creator = models.ForeignKey(USER_MODEL, blank=True)
    creator_ip = models.GenericIPAddressField(_('Creator IP'))

    class Meta:
        verbose_name = _('Revision')
        verbose_name_plural = _('Revisions')
        ordering = ('-created_on',)
        get_latest_by = 'created_on'

    def save(self, *args, **kwargs):
        self.rendered = markdown(self.content)

        super().save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return 'simplewiki.detail', (), {'slug': self.document.slug}

    def __str__(self):
        args = self.document.title, self.content[:50]
        return '%s: %s' % args
