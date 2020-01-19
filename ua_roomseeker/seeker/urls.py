from django.urls import path
from . import views

app_name = 'seeker'

urlpatterns = [
    #/seeker/
    path('', views.IndexView.as_view(), name='index') ,

    #/seeker/building/71/
    path('building/<int:pk>/', views.BuildingDetailView.as_view(), name='building-detail'),

    #/seeker/building/add
    path('building/add/', views.BuildingCreate.as_view(), name='building-add'),

    # #/seeker/building/2/update
    # path('building/<int:pk>/update', views.BuildingUpdate.as_view(), name='album-update'),

    # #/seeker/building/2/delete/
    # path('building/<int:pk>/delete/', views.BuildingDelete.as_view(), name='album-delete'),

    #/seeker/classroom/add
    path('classroom/add/', views.ClassroomCreate.as_view(), name='classroom-add'),

]