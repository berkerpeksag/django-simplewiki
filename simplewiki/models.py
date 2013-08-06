from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Document(models.Model):

    author = models.ForeignKey(User)
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=100, unique=True)
    text = models.TextField()
    is_published = models.BooleanField(default=False, verbose_name="Publish?")
    created_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Document, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return 'document_detail', (), {'slug': self.slug}
