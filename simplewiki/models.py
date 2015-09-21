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
    creator = models.ForeignKey(USER_MODEL, blank=True)

    content = models.TextField(_('Content'))
    rendered = models.TextField(blank=True, editable=False)  # HTML version of the content

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
        self.rendered = markdown(self.content)

        super().save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return 'simplewiki.detail', (), {'slug': self.slug}

    def __str__(self):
        return self.title
