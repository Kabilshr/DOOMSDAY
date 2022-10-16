#year digit split
#TODO improve for larger years
def year_split(year):
    year = str(year)
    global century
    global num_year
    century = int(year[0:-2])
    num_year =int(year[-1:-3:-1])

#tells if it is a leap year.
def lp_year(year):
    global is_lp_year
    year = int(year)
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                is_lp_year = True
            else:
                is_lp_year = False
        else:
            is_lp_year = True
    else:
        is_lp_year = False

#find century code
def cent_code(century):
    global century_code
    tuesday = []
    sunday = []
    friday = []
    wednesday = []
    #CREATION OF LIST
    # tuesday
    for A in range(0, 9999, 4):
        tuesday.append(A)
    # sunday
    for B in range(1, 9999, 4):
        sunday.append(B)
    # friday
    for C in range(2, 9999, 4):
        friday.append(C)
    # wednesday
    for D in range(3, 9999, 4):
        wednesday.append(D)
    
    #finding code from list
    if century in tuesday:
        century_code = 2
        
    elif century in sunday:
        century_code = 0
        
    elif century in friday:
        century_code = 5
        
    elif century in wednesday:
        century_code = 3

#TODO some problem need to be figured out
def yr_code(num_year):
    global year_code
    if num_year == 0:
        year_code = century_code
    else:
        yr_div_12 = int(num_year //12) #how many times 12 goes into the year
        yr_div_rem = int(num_year % 12) #remainder
        rem_div = int(yr_div_rem // yr_div_12) #how many times quotent goes in remainder
        Y = century_code + yr_div_12 + yr_div_rem + rem_div #adding all up
        if Y > 6 :
            year_code = Y % 7
        else:
            year_code = Y

#difference from doomsday ps
#credit for this function: Krish
def days_frm_dmsdy(date, month, is_lp_year):
    global dif_date
    global doomsday_mth #doomsday of a month
    if month == 1:
        if is_lp_year == True:
            doomsday_mth = 4
            dif_date = date - doomsday_mth
        else:
            doomsday_mth = 3
            dif_date = date - doomsday_mth
    elif month == 2:
        if is_lp_year == True:
            doomsday_mth = 29
            dif_date = date - doomsday_mth
        else:
            doomsday_mth = 28
            dif_date = date - doomsday_mth
    elif month == 3:
        doomsday_mth = 14
        dif_date = date - doomsday_mth
    elif month == 4:
        doomsday_mth = 4
        dif_date = date - doomsday_mth
    elif month == 5:
        doomsday_mth = 9
        dif_date = date - doomsday_mth
    elif month == 6:
        doomsday_mth = 6
        dif_date = date - doomsday_mth
    elif month == 8:
        doomsday_mth = 8
        dif_date = date - doomsday_mth
    elif month == 7:
        doomsday_mth = 11
        dif_date = date - doomsday_mth
    elif month == 9:
        doomsday_mth = 5
        dif_date = date - doomsday_mth
    elif month == 10:
        doomsday_mth = 10
        dif_date = date - doomsday_mth
    elif month == 11:
        doomsday_mth = 7
        dif_date = date - doomsday_mth
    elif month == 12:
        doomsday_mth = 12
        dif_date = date - doomsday_mth

#find day*
def fnd_day(dif_date):
    global day_cd
    if dif_date == 0:
        day_cd = year_code
    elif dif_date < 0:
        day_cd = abs(dif_date + year_code)
        day_cd = dif_date % 7
    
    if dif_date > 6:
        day_cd = dif_date % 7
    else:
        day_cd = dif_date


#MAIN PROGRAM
alert = "IMPORTANT NOTE!"
alert = alert.center(40, "~")
thanks = "THANK YOU"
thanks = thanks.center(40, "~")
print("Welcome to DOOMSDAY! This is a program that tells you day of any date.")
imp_msg = "{0}\nIF YOU ENTER ANYTHING OTHER THAN INTEGERS CHARACTERS, THE PROGRAM WILL GIVE AN ERROR BECAUSE I HAVE NOT WRITTEN ANY ERROR HANDLING CODE. IF YOU ENTER IT BY MISTAKE THEN PLEASE RESTART THE PROGRAM\n{1}".format(alert, thanks)
imp_msg = imp_msg.rjust(20, " ")
print(imp_msg)
start = input("Are you ready to get started?y/n  ")
if str.lower(start) == "n":
    print("Byeee!")
    quit
else:
    x = 0
    while(True): #main program loop
        #loop quit code.
        x+=1
        if x > 1:
            again = input("Do you want to try again? \n enter n to quit... y/n  ")
        else:
            again = "y" #defines again as y to prevent error
        #try again loop break
        if str.lower(again) == "n":
            print("THANK YOU! for trying out our program") #exit program
            break
        else:#main program order
            #inputs
            date = int(input("Enter date: "))
            if date > 31:
                print("There can't be more than 31 days in a months.")
                print("This caused an error so please run the program again.")
                break
            month = int(input("Enter month: "))
            if month > 12:
                print("There can't be more than 12 months.")
                print("This caused an error so please run the program again.")
                break

            if month == 2:
                if is_lp_year == True:
                    if date > 29:
                        print("Febuary doesn't have more than 29 days.")
                        print("This caused an error so please run the program again.")
                else:
                    if date > 28:
                        print("Febuary doesn't have more than 28 days as it is not a leap year.")
                        print("This caused an error so please run the program again.")
            
            year = int(input("Enter year: "))
                        
            #slice year
            year_split(year)

            #check leap year
            lp_year(year)

            #get century code
            cent_code(century)

            #get year code
            yr_code(num_year)

            #get difference in days
            days_frm_dmsdy(date, month, is_lp_year)

            #find day number
            fnd_day(dif_date)

            day_list = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
            #credit for this function: Krish
            if day_cd >= 0:
                day = day_list[day_cd + 1]
            elif day_cd < 0:
                day = day_list[(day_cd + 8)] #yr_code problem fix

            print(day)