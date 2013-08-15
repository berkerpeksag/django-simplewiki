from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView

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


class DocumentRevision(LoginRequiredMixin, CreateView):
    model = Revision
    form_class = RevisionForm

    @property
    def document(self):
        return Document.objects.get(slug=self.kwargs['slug'])

    def get_initial(self):
        initial = super(DocumentRevision, self).get_initial()
        initial['content'] = self.document.current_revision.content
        return initial

    def form_valid(self, form):
        form.instance.creator = self.request.user
        form.instance.document = self.document
        return super(DocumentRevision, self).form_valid(form)

    def get_context_data(self, **kwargs):
        return super(DocumentRevision,
                     self).get_context_data(doc=self.document,
                                            **kwargs)
