from __future__ import print_function, unicode_literals

from django.shortcuts import redirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView

from .forms import DocumentForm, RevisionForm, RevisionFormSet
from .mixins import LoginRequiredMixin
from .models import Document, Revision


class DocumentIndex(ListView):
    queryset = Document.objects.published()
    context_object_name = 'docs'
    template_name = 'simplewiki/document_list.html'


class DocumentDetail(DetailView):

    queryset = Document.objects.published()
    context_object_name = 'doc'
    template_name = 'simplewiki/document_detail.html'


class DocumentCreate(LoginRequiredMixin, CreateView):
    model = Document
    form_class = DocumentForm

    def get_context_data(self, **kwargs):
        context = super(DocumentCreate, self).get_context_data(**kwargs)
        # TODO: Consider handling this in DocumentCreate.post()
        if self.request.POST:
            context['doc_rev_form'] = RevisionFormSet(self.request.POST, instance=self.object)
        else:
            context['doc_rev_form'] = RevisionFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        doc_rev_form = context['doc_rev_form']
        if form.is_valid() and doc_rev_form.is_valid():
            self.object = form.save()
            doc_rev_form.instance = self.object
            x = doc_rev_form.save(commit=False)
            x[0].creator = self.request.user
            x[0].save()
            return redirect(self.object.get_absolute_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class DocumentAddRevision(LoginRequiredMixin, CreateView):
    model = Revision
    form_class = RevisionForm

    @property
    def document(self):
        return Document.objects.get(slug=self.kwargs['slug'])

    def get_initial(self):
        initial = super(DocumentAddRevision, self).get_initial()
        initial['content'] = self.document.current_revision.content
        return initial

    def form_valid(self, form):
        form.instance.creator = self.request.user
        form.instance.document = self.document
        return super(DocumentAddRevision, self).form_valid(form)

    def get_context_data(self, **kwargs):
        return super(DocumentAddRevision,
                     self).get_context_data(doc=self.document,
                                            **kwargs)
