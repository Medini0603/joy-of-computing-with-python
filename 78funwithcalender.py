import calendar

def checkleap(year):
    if(year%100==0):
        if(year%400==0):
            return True
        else:
            return False
    if(year%4==0):
        return True
    else:
        return False

def checkdate(d,m,y):
    if(m==2):
        if(checkleap(y)):
            if(d<30):
                return True
            else:
                return False
        else:
            if(d<29):
                return True
            else:
                return False
    elif(m<8):
        if(m%2==0):
            if(d<31):
                return True
            else:
                return False
        else:
            if(d<32):
                return True
            else:
                return False
    elif(m>=8):
        if(m%2==0):
            if(d<32):
                return True
            else:
                return False
        else:
            if(d<31):
                return True
            else:
                return False

def daydisp(index):
    days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    return(days[index])

while(1):
    year=int(input("Enter year after 1970 "))
    if(year<1970):
        print("Please enter a year after 1970 ")
    else:
        break

while(1):
    month=int(input("Enter the month (1 to 12) "))
    if(month<=0 or month>12):
        print("Please enter a valid month ")
    else:
        break

while(1):
    date=int(input("Enter the date "))
    if(date<=0 or checkdate(date,month,year)):
        break
    else:
        print("Please enter a valid date according to month and year ")

index=calendar.weekday(year,month,date)
print(date," / ",month," / ",year," falls on ",daydisp(index))




