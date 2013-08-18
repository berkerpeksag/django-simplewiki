from django.conf import settings
from django.db import models
from django.utils.encoding import smart_unicode
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify

from markdown import markdown

from .managers import DocumentManager


USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

MARKUPS = (
    (u'rst', u'reStructuredText'),
    (u'md', u'Markdown'),
)


class Document(models.Model):

    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=100, unique=True)

    is_published = models.BooleanField(_('Publish?'), default=False)
    markup = models.CharField(max_length=3, choices=MARKUPS, default='md')

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    current_revision = models.ForeignKey('Revision', null=True,
                                         related_name='current_for+')

    # List of users that have contributed to this document.
    contributors = models.ManyToManyField(USER_MODEL)

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
    def rendered(self):
        return self.current_revision.rendered

    @models.permalink
    def get_absolute_url(self):
        return 'document_detail', (), {'slug': self.slug}

    def __unicode__(self):
        return smart_unicode(self.title)


class Revision(models.Model):

    document = models.ForeignKey(Document, related_name='revisions')

    summary = models.CharField(max_length=150)

    content = models.TextField(_('Content'))
    rendered = models.TextField(blank=True)  # HTML version of the content

    created_on = models.DateTimeField(auto_now_add=True)

    creator = models.ForeignKey(USER_MODEL, related_name='created_revisions')

    def save(self, *args, **kwargs):
        if self.document.markup == 'md':
            self.rendered = markdown(self.content)
        else:
            self.rendered = self.content

        super(Revision, self).save(*args, **kwargs)

        if not self.document.current_revision or \
           self.document.current_revision.id < self.id:
            contributors = self.document.contributors.all()
            new_revs = self.document.revisions.filter(id__gt=self.document.id)
            new_contributors = set([r.creator for r in new_revs.select_related('creator')])

            for user in new_contributors:
                if user not in contributors:
                    self.document.contributors.add(user)

        self.document.current_revision = self
        self.document.save()

    @models.permalink
    def get_absolute_url(self):
        return 'document_detail', (), {'slug': self.document.slug}

    def __unicode__(self):
        return smart_unicode('%s #%s: %s' % (self.document.title,
                               self.id, self.content[:50]))
