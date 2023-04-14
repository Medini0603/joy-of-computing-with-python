import random
import datetime
birthday=[]

i=0
while(i<50):
    year=random.randint(1900,2022)
    # because oldest person lived was 122 years 
    if(year%4==0 and year%100!=0 or year%400==0):
        leap=1
    else:
        leap=2
    month=random.randint(1,12)
    if(month==2 and leap==1):
        day=random.randint(1,29)
    elif(month==2 and leap==0):
        day=random.randint(1,28)
    elif(month==7 or month==8):
        day=random.randint(1,31)
    elif(month%2!=0 and month<7):
        day=random.randint(1,31)
    elif(month%2==0 and month>7 and month<12):
        day=random.randint(1,31)
    else:
        day=random.randint(1,30)
    date=datetime.date(year,month,day)
    dayofyear=date.timetuple().tm_yday
    i=i+1
    birthday.append(dayofyear)

birthday.sort()
print(birthday)

# we get collision in 50 people only 