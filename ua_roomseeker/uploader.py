from seeker.models import Building, Classroom, Time
import json

DJANGO_SETTINGS_MODULE = ua_roomseeker.settings

f = open('../data/A.json', 'r')
data = f.read()
jsondata = json.loads(data)

#create the building
building = Building(BuildingName='A')
building.save()
for day in jsondata:
    for room in jsondata[day]:
        classroom = Classroom(building = 'A', ClassroomName=jsondata[day][room])
        classroom.save()
        for time in jsondata[day][room]:
            time = Time(building='A', classroom=jsondata[day][room], DayofWeek=day, TimeValue=jsondata[day][room][time])
            time.save()

    

