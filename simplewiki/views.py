from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from .forms import DocumentForm
from .mixins import AddUserObjectMixin, LoginRequiredMixin
from .models import Document, Revision


class DocumentIndex(ListView):
    queryset = Document.objects.published()
    context_object_name = 'docs'
    template_name = 'simplewiki/document_list.html'


class RevisionList(DetailView):
    queryset = Document.objects.published()
    context_object_name = 'doc'
    template_name = 'simplewiki/document_revisions.html'


class DocumentDetail(DetailView):
    queryset = Document.objects.published()
    context_object_name = 'doc'
    template_name = 'simplewiki/document_detail.html'


class RevisionDetail(DetailView):
    model = Revision
    context_object_name = 'rev'
    template_name = 'simplewiki/revision_detail.html'


class DocumentCreate(LoginRequiredMixin, AddUserObjectMixin, CreateView):
    model = Document
    form_class = DocumentForm

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class DocumentUpdate(LoginRequiredMixin, AddUserObjectMixin, UpdateView):
    model = Document
    form_class = DocumentForm
    template_name = 'simplewiki/document_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'update'
        return context
