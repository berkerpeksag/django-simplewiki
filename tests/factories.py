import factory

from django.conf import settings

from simplewiki.models import Document


class UserFactory(factory.DjangoModelFactory):

    class Meta:
        model = settings.AUTH_USER_MODEL

    username = 'foo-bar'


class DocumentFactory(factory.DjangoModelFactory):

    class Meta:
        model = Document

    title = factory.Sequence(lambda n: 'Document Title #{}'.format(n))
    slug = factory.Sequence(lambda n: 'document-title-{}'.format(n))
    content = factory.Sequence(lambda n: 'Document content #{}'.format(n))
    creator = factory.SubFactory(UserFactory)
