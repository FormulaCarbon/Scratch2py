from datetime import datetime
from scratch2py import Scratch2Py
import pytz
print('Enter Scratch Credentials Below')
username = input('  Username: ')
password = input('  Password: ')
s2py = Scratch2Py(username, password)
cloudproject = s2py.scratchConnect('677826748')# This is not the actual PlutoniumNetwork ID, but the v0.4.3 UI update ID
while 1:

    requestedtz = input('Input Timezone (For a list of timezones, type //ALLTZ): ')
    if requestedtz == '//ALLTZ':
        alltz = pytz.all_timezones
        print('Available Timezones:', alltz)
        requestedtz = input('Input Timezone (For a list of timezones, type //ALLTZ): ')

    tzinput = pytz.timezone(requestedtz)

    datetimeintz = datetime.now(tzinput)
    truetime=s2py.encode(datetimeintz.strftime("%H:%M:%S"))
    cloudproject.setCloudVar('Timefroms2py', truetime)

    print("Current time in " +requestedtz+" is :", datetimeintz.strftime("%H:%M:%S"))
    print('')
