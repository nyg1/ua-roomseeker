from django.urls import path
from . import views

app_name = 'seeker'

urlpatterns = [
    #/seeker/
    path('', views.IndexView.as_view(), name='index') ,

    #/seeker/building/71/
    path('building/<int:pk>/', views.BuildingDetailView.as_view(), name='building-detail'),

    #/seeker/album/add
    path('building/add/', views.BuildingCreate.as_view(), name='building-add'),

    # #/seeker/album/2/
    # path('album/<int:pk>/update', views.AlbumUpdate.as_view(), name='album-update'),

    # #/seeker/album/2/delete/
    # path('album/<int:pk>/delete/', views.AlbumDelete.as_view(), name='album-delete'),

    #/seeker/song/add
    path('classroom/add/', views.ClassroomCreate.as_view(), name='classroom-add'),
]