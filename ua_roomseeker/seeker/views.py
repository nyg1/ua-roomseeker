from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Building, Classroom

class IndexView(generic.ListView):
    template_name = 'seeker/index.html'
    context_object_name = 'all_Buildings'

    def get_queryset(self):
        return Building.objects.all()

# class DetailView(generic.DetailView):
#     model = Album
#     template_name = 'music/detail.html'

# class AlbumCreate(CreateView):
#     model = Album
#     fields = ['artist', 'album_title', 'genre', 'album_logo']

# class AlbumUpdate(UpdateView):
#     model = Album
#     fields = ['artist', 'album_title', 'genre', 'album_logo']

# class AlbumDelete(DeleteView):
#     model = Album
#     success_url = reverse_lazy('music:index')

# class SongCreate(CreateView):
#     model = Song
#     fields = ['album', 'file_type', 'song_title']
