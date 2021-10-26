from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Entry
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.
class EntryListView(ListView):
    model = Entry
    queryset = Entry.objects.all().order_by('-date_created')
    context_object_name = 'entry_list'


class EntryDetailView(DetailView):
    model = Entry
    context_object_name = 'entry_detail'


class EntryCreateView(SuccessMessageMixin, CreateView):
    model = Entry
    fields = ['title', 'content', 'high_priority']
    success_url = reverse_lazy('Diary:entry-list')
    success_message = 'Your %(title)s Entry Was Created Successfully'


class EntryUpdateView(SuccessMessageMixin, UpdateView):
    model = Entry
    fields = ['title', 'content', 'high_priority']
    success_message = 'Your %(title)s Entry Was Updated Successfully'

    def get_success_url(self):
        return reverse_lazy("Diary:entry-detail", kwargs={"pk": self.object.id})


class EntryDeleteView(DeleteView):
    model = Entry
    success_url = reverse_lazy('Diary:entry-list')
    success_message = 'Your Entry Was Deleted!'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)
