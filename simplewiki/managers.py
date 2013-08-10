from django.db import models


class DocumentManager(models.Manager):

    def published(self):
        return self.get_query_set().filter(is_published=True)
