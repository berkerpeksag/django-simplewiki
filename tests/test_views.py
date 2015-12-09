from django.test import TestCase
from django.core.urlresolvers import reverse

from . import factories


class ViewTests(TestCase):

    def test_index(self):
        response = self.client.get(reverse('simplewiki.index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No documents are available.')

    def test_redirect_to_login(self):
        urls = [
            reverse('simplewiki.create'),
            reverse('simplewiki.update', kwargs=dict(slug='foo')),
        ]
        for url in urls:
            with self.subTest(url=url):
                response = self.client.get(url)
                self.assertEqual(response.status_code, 302)

    def test_document_detail_raises_404(self):
        response = self.client.get(reverse('simplewiki.detail',
                                   kwargs=dict(slug='foo')))
        self.assertEqual(response.status_code, 404)

    def test_update_redirect_to_login(self):
        d = factories.DocumentFactory(title='title', slug='title')
        response = self.client.get(reverse('simplewiki.update',
                                   kwargs=dict(slug='title')))
        self.assertEqual(response.status_code, 302)
