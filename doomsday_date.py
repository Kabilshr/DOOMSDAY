#is_lp_month = status of leap month
#dday is the number of days the day of a date is away from doomsday
#date
#month
is_lp_year = True

date = int(input('Enter date:'))
month = int(input('Enter the month:'))
doomsday = int(input('enter doomsday:'))
def closest(llst, month):
	return llst[min(range(len(llst)), key = lambda i: abs(llst[i]-month))]
llst = [1,2,3,4,5,6,7,8,9,10,11,12]
doom_month = int(closest(llst, month))
k = int((llst.index(doom_month)))
if (month - doom_month) < 0:
    doom_month = llst[(k - 1)]
else:
    doom_month = int(closest(llst, month))
print(doom_month)

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
    def clos(lst, dday):
	    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-dday))]
    
    
    lst = [0, 7, 14, 21, 27, 35, 42, 49, 54, 63, 70, 77, 84, 91, 98]
    k=int((clos(lst, dday)))
    x=int((lst.index(k)))
    if (dday - k) < 0:
        k = lst[(x - 1)]
        print(k)
    else:
        k = int(clos(lst, dday))
    day = dday - k
    day_date = doomsday + day
elif dday < 0:
    def clos(lst, dday):
	    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-dday))]
    
    lst = [-35,-27,-21,-14,-7, 0]
    k=int((clos(lst, dday)))
    x=int((lst.index(k)))
    day = abs(dday - k)
    day_date = doomsday - day
elif dday == 0:
    day_date = doomsday

day_list = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
if day_date>=0:
    val = day_list[day_date]
elif day_date<0:
    val = day_list[(day_date+7)]

print(val)
