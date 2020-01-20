from seeker.models import Building, Classroom, Time
import json
import os

os.chdir('../data')
fileList = os.listdir()

#loops through each json file
for jsonfile in fileList:
    #opens the jsonfile and loads the data
    f = open(jsonfile, 'r')
    data = f.read()
    jsondata = json.loads(data)
    #create the building
    building = Building(BuildingName=os.path.splitext(jsonfile)[0])
    building.save()
    for day in jsondata:
        for room in jsondata[day].keys():
            #creates each classroom, adding one only if one doesn't exist
            classroom = Classroom.objects.get_or_create(building = Building.objects.get(BuildingName = os.path.splitext(jsonfile)[0]), ClassroomName = os.path.splitext(jsonfile)[0] + ' - ' + room)
            for time in jsondata[day][room]:
                #creates each time 
                time = Time(building=Building.objects.get(BuildingName = os.path.splitext(jsonfile)[0]), classroom=Classroom.objects.get(ClassroomName = os.path.splitext(jsonfile)[0] + ' - ' + room), DayofWeek=day, TimeValue=time)
                time.save()

#IMPORTANT!!!!!!!
# This program must be run inside a python manage.py shell for it to work, in the future a fix may be found, 
# but for the time being, follow these steps:
# 1. open powershell and navigate to the folder that contains this file 
# 2. type in "python manage.py shell"
# 3. copy and paste the code into the shell and press enter 
# 4. wait time is around 5 minutes

