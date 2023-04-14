from datetime import datetime as dt
print(dt.now())

# to get the time of a particular time zone 
import pytz
tz=pytz.timezone('Singapore')
print(dt.now(tz))

# print(pytz.all_timezones)
print(len(pytz.all_timezones))

import calendar
# calendar.weekday gives monday as 0 tue as 1 and so on... 
print(calendar.weekday(2002,6,3))

# to print a specific months calender of a specific year 
print(calendar.month(2022,3))

# to print one years calender 
print(calendar.prcal(2022))

# to find coordinated universal time.
print(dt.utcnow())