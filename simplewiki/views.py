from django.views.generic import DetailView, ListView

from .models import Document


class DocumentDetailView(DetailView):

    model = Document
    context_object_name = 'doc'
    template_name = 'simplewiki/document.html'
