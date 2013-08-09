from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from markdown import markdown


MARKUPS = (
    (u'rst', u'reStructuredText'),
    (u'md', u'Markdown'),
)


class Document(models.Model):

    author = models.ForeignKey(User)
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=100, unique=True)
    text = models.TextField()
    is_published = models.BooleanField(default=False, verbose_name='Publish?')
    created_on = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    markup = models.CharField(max_length=3, choices=MARKUPS, default='md')

    class Meta:
        ordering = ['-update_date']
    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Document, self).save(*args, **kwargs)

    def render(self):
        if self.markup == 'md':
            return markdown(self.text)
        return self.text


    @models.permalink
    def get_absolute_url(self):
        return 'document_detail', (), {'slug': self.slug}
