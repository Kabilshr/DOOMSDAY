#is_lp_month = status of leap month
#dday is the number of days the day of a date is away from doomsday
#date
#month
is_lp_year = True

date = int(input('Enter date:'))
doom_month = int(input('Enter the month:'))
doomsday = 1

if doom_month == 1:
    if is_lp_year == True:
        dday = date - 4
    else:
        dday = date - 3
elif doom_month == 2:
    if is_lp_year == True:
        dday = date - 29
    else:
        dday = date - 28
elif doom_month == 3:
    dday = date - 14
elif doom_month == 4:
    dday = date - 4
elif doom_month == 5:
    dday = date - 9
elif doom_month == 6:
    dday = date - 6
elif doom_month == 8:
    dday = date - 8
elif doom_month == 7:
    dday = date - 11
elif doom_month == 9:
    dday = date - 5
elif doom_month == 10:
    dday = date - 10
elif doom_month == 11:
    dday = date - 7
elif doom_month == 12:
    dday = date - 12
if dday > 0:
    day = dday % 7
    day_date = doomsday + day
elif dday < 0:
    day = abs(dday % -7)
    day_date = doomsday - day
    
elif dday == 0:
    day_date = doomsday

day_list = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
if day_date>=0:
    val = day_list[day_date]
elif day_date<0:
    val = day_list[(day_date+7)]

print(val)
