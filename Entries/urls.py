from django.urls import path
from . import views

app_name = 'Diary'
urlpatterns = [
    path("", views.EntryListView.as_view(), name='entry-list'),
    path("entry/<int:pk>/", views.EntryDetailView.as_view(), name='entry-detail')
    
]
