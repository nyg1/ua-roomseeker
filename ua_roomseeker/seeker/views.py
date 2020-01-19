from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Building, Classroom

from django.shortcuts import render
from django.http import HttpResponse

class IndexView(generic.ListView):
    template_name = 'seeker/index.html'
    context_object_name = 'all_Buildings'

    def get_queryset(self):
        return Building.objects.all()

class BuildingDetailView(generic.DetailView):
    model = Building
    template_name = 'seeker/building-detail.html'

class BuildingCreate(CreateView):
    model = Building
    fields = ['BuildingName']

# class AlbumUpdate(UpdateView):
#     model = Album
#     fields = ['artist', 'album_title', 'genre', 'album_logo']

# class AlbumDelete(DeleteView):
#     model = Album
#     success_url = reverse_lazy('music:index')

class ClassroomCreate(CreateView):
    model = Classroom
    fields = ['building', 'ClassroomName']

def homepage(request):
    response = render(request, 'seeker/homepage.html')
    return response