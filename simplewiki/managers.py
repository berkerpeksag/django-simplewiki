from django.db import models


class DocumentManager(models.Manager):

    def published(self):
        return self.get_queryset().filter(is_published=True)
