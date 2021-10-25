from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Entry


# Create your views here.
class EntryListView(ListView):
    model = Entry
    queryset = Entry.objects.all().order_by('-date_created')
    context_object_name = 'entry_list'


class EntryDetailView(DetailView):
    model = Entry
    context_object_name = 'entry_detail'

class EntryCreateView(CreateView):
    model = Entry
    fields = ['title', 'content', 'high_priority']
    success_url = reverse_lazy('Diary:entry-list')
    context_object_name = 'entry_create'


class EntryUpdateView(UpdateView):
    model = Entry
    fields = ['title', 'content', 'high_priority']
    context_object_name = 'entry_update'

    def get_success_url(self):
        return reverse_lazy("Diary:entry-detail", {"pk": self.entry.id})


class EntryDeleteView(DeleteView):
    model = Entry
    success_url = reverse_lazy('Diary:entry-list')

