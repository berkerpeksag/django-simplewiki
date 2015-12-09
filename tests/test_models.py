from django.test import TestCase

from .factories import DocumentFactory


class ModelTests(TestCase):

    def test_create_document(self):
        d = DocumentFactory()
        self.assertEqual(d.title, 'Document Title #0')
        self.assertEqual(d.slug, 'document-title-0')
        self.assertEqual(d.creator.username, 'foo-bar')
