from django.db import models
from django.urls import reverse

# red has the primary key of 1
class Building(models.Model):
    BuildingName = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('seeker:building-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.BuildingName

#foreign key for this is also 1 to link it
#on_delete=models.cascade means that if you delete the building, we also delete all classrooms linked to that
class Classroom(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    ClassroomName = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('seeker:index')

    def __str__(self):
        return self.ClassroomName

class Time(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    DayofWeek = models.CharField(max_length=1)
    TimeValue = models.IntegerField()

    def get_absolute_url(self):
        return reverse('seeker:index')

    def __str__(self):
        return self.DayofWeek + '-' + str(self.TimeValue)
