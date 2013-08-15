from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from extra_views import InlineFormSetView

from .forms import RevisionForm
from .mixins import LoginRequiredMixin
from .models import Document, Revision


class DocumentIndex(ListView):

    queryset = Document.objects.published()
    context_object_name = 'docs'
    template_name = 'simplewiki/index.html'


class DocumentDetail(DetailView):

    model = Document
    context_object_name = 'doc'
    template_name = 'simplewiki/document_detail.html'


class DocumentRevision(CreateView):
    model = Revision
    form_class = RevisionForm

    def form_valid(self, form):
        form.instance.creator = self.request.user
        form.instance.document = Document.objects.get(slug=self.kwargs['slug'])
        return super(DocumentRevision, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(DocumentRevision, self).get_context_data(**kwargs)
        context['doc'] = Document.objects.get(slug=self.kwargs['slug'])
        return context
