from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Building, Classroom

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'seeker/index.html'
    context_object_name = 'all_Buildings'

    def get_queryset(self):
        print(Building.objects.all())
        return Building.objects.all()