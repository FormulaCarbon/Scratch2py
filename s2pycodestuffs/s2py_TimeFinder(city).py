from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
from scratch2py import Scratch2Py
import pytz
print('Enter Scratch Credentials Below')
username = input('  Username: ')
password = input('  Password: ')
s2py = Scratch2Py(username, password)
cloudproject = s2py.scratchConnect('677826748')# This is not the actual PlutoniumNetwork ID, but the v0.4.3 UI update ID
while 1:
    geolocator = Nominatim(user_agent="geoapiExercises")

    lad = input('Type in location(city): ')
    location = geolocator.geocode(lad)
    obj = TimezoneFinder()

    # returns timezone
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    print("Time Zone : ", result)

    tzinput = pytz.timezone(result)

    datetimeintz = datetime.now(tzinput)
    truetime=s2py.encode(datetimeintz.strftime("%H:%M:%S"))
    cloudproject.setCloudVar('Timefroms2py', truetime)

    print("Current time in " +lad+" is :", datetimeintz.strftime("%H:%M:%S"))
    print('')
