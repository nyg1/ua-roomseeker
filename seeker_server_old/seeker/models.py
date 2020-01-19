from django.db import models
from django.urls import reverse

# red has the primary key of 1
class Building(models.Model):
    bname = models.CharField(max_length=50)
    bid = models.AutoField(primary_key=True)

    def get_absolute_url(self):
        return reverse('seeker:building-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.bname

#foreign key for this is also 1 to link it
#on_delete=models.cascade means that if you delete the building, we also delete all classrooms linked to that
class Classroom(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    cname = models.CharField(max_length=50)
    cid = models.AutoField(primary_key=True)

    def get_absolute_url(self):
        return reverse('seeker:index')

    def __str__(self):
        return self.cname

class Time(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    tid = models.AutoField(primary_key=True)
    day = models.CharField(max_length=1)
    time = models.IntegerField()

    def get_absolute_url(self):
        return reverse('seeker:index')

    def __str__(self):
        return self.day + '-' + str(self.time)
