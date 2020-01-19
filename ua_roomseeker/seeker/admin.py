from django.contrib import admin
from .models import Building, Classroom, Time

# Register your models here.
admin.site.register(Building)
admin.site.register(Classroom)
admin.site.register(Time)