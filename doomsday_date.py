#is_lp_month = status of leap month
#date
#mont
is_lp_year = True

date = int(input('Enter date:'))
month = int(input('Enter the month:'))

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
    val = dday - k
elif dday < 0:
    def clos(lst, dday):
	    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-dday))]
    lst = [-35,-27,-21,-14,-7, 0]
    y=int((clos(lst, dday)))
    x=int((lst.index(y)))
    if (dday - y) < 0:
        y = lst[(x - 1)]
        print(y)
    else:
        y = int(clos(lst, dday))
    val = dday - y
    print(y)
elif dday == 0:
