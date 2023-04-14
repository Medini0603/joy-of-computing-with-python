# tm_yday(Day of Year)	1 to 366
import datetime

#to convert numbers to 
dd=datetime.date(2022,8,17)
# dd1=datetime.date(17,8,2022) --->wrong format
# datetime.date(year: int, month: int, day: int)
# format for date function
print(dd)
day=dd.timetuple().tm_yday
print("hihihi",day)

print(datetime.date.today())
print(datetime.date.today().strftime("%Y"))
print(datetime.date.today().strftime("%B"))
print(datetime.date.today().strftime("%d"))
print(datetime.date.today().strftime("%W")) #week number of the year
print(datetime.date.today().strftime("%w")) #weekday number
print(datetime.date.today().strftime("%j")) #day of year
print(datetime.date.today().strftime("%A")) #day of week
print(datetime.datetime.now()) #currentdate and time


