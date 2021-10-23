from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Entry


# Create your views here.
class EntryListView(ListView):
    model = Entry
    queryset = Entry.objects.all().order_by('-date_created')
    context_object_name = 'entry_list'


class EntryDetailView(DetailView):
    model = Entry
    context_object_name = 'entry_detail'

