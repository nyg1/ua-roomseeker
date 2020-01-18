from django.urls import path
from . import views

app_name = 'seeker'

urlpatterns = [
    #/seeker/
    path('', views.IndexView.as_view(), name='index') ,

    # #/seeker/71/
    # path('album/<int:pk>/', views.DetailView.as_view(), name='detail'),

    # #/seeker/album/add
    # path('album/add/', views.AlbumCreate.as_view(), name='album-add'),

    # #/seeker/album/2/
    # path('album/<int:pk>/update', views.AlbumUpdate.as_view(), name='album-update'),

    # #/seeker/album/2/delete/
    # path('album/<int:pk>/delete/', views.AlbumDelete.as_view(), name='album-delete'),

    # #/seeker/song/add
    # path('song/add', views.SongCreate.as_view(), name='song-add'),
]