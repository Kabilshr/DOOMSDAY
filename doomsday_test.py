#for finding closest century
def closest(llst, year):
	return llst[min(range(len(llst)), key = lambda i: abs(llst[i]-year))]
llst = [1700, 1800, 1900, 2000, 2100, 2200]
year = int(input('Enter the year:'))
ref_yrs = int(closest(llst, year))
k = int((llst.index(ref_yrs)))
if (year - ref_yrs) < 0:
    ref_yrs = llst[(k - 1)]
else:
    ref_yrs = int(closest(llst, year))

#Finding doomsday
if ref_yrs == 1700 or 2100 or 2500:
    doomsday =  0 + (year - ref_yrs) + int((year - ref_yrs)/4)
elif ref_yrs == 1800 or 2200 or 2600:
    doomsday =  5 + (year - ref_yrs) + int((year - ref_yrs)/4)   
elif ref_yrs == 1900 or 2300 or 2700:
    doomsday =  3 + (year - ref_yrs) + int((year - ref_yrs)/4)  
elif ref_yrs == 2000 or 2400 or 2800:
    doomsday =  2 + (year - ref_yrs) + int((year - ref_yrs)/4)
else:
    print("..")
    
def clos(lst, doomsday):
	return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-doomsday))]
lst = [0, 7, 14, 21, 27, 35, 42, 49, 54, 63, 70, 77, 84, 91, 98]
k=int((clos(lst, doomsday)))
x=int((lst.index(k)))
if (doomsday - k) < 0:
    k = lst[(x - 1)]
    print(k)
else:
    k = int(clos(lst, doomsday))
val = doomsday - k
final_value = print(f'The DOOMSDAY of the year {year} is {val}')
