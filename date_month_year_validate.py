# validate the input year, month and day and give the output date without using datetime module.
months={1:31,2:{'leap':29,'notleap':28},3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

year=eval(input("enter year"))
# check for leap year or not
def check_for_leap(year):
    if (year%100!=0 and year%2==0) or (year%400==0):
        leap_year= 'leap'
    else:
        leap_year= 'notleap'
    return leap_year
# print(leap_year)

ver=True
while ver:
    month = eval(input('enter a month from 1 to 12'))
    if month in range(1,13):
        ver=False
    else:
        print('Enter valid month')
leap_year= check_for_leap(year)
val=True
while val:
    
    day = eval(input("enter a day"))
    if month!=2:
        print(months[month])
        if day not in range(1,months[month]+1):
            print("enter a valid day")
        else:
            val=False
    else:
        print(months[month][leap_year])
        if day in range(1,months[month][leap_year]+1):
            val=False
            
        else:
            print('enter a valid day')
print("date in format of day,month,year is {}/{}/{}".format(day,month,year))       

