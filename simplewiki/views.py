from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView

from .forms import DocumentForm
from .models import Document


class IndexView(ListView):

    context_object_name = 'docs'
    template_name = 'simplewiki/index.html'

    def get_queryset(self):
        return Document.objects.filter(is_published=True)


class DocumentDetailView(DetailView):

    model = Document
    context_object_name = 'doc'
    template_name = 'simplewiki/document_detail.html'


class DocumentUpdate(UpdateView):

    model = Document
    form_class = DocumentForm
