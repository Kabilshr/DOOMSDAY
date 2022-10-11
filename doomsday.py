#date limit function
def date_limit(date):
    if date > 31:
        print("There can't be more than 31 days in a months.")
    else:
        return date

#month limit function
def month_limit(month):
    if month > 12:
        print("There can't be more than 12 months.")
    else:
        return month

#febuary day limit
def feb_limit(date, month):
    if month == 2:
        if is_lp_year == True:
            if date > 29:
                print("Febuary doesn't have more than 29 days.")
            else:
                pass
        else:
            if date > 28:
                print("Febuary doesn't have more than 28 days as it is not a leap year.")
            else:
                pass
    else:
        pass

#year digit split
def year_split(year):
    year = str(year)
    global centuary
    global num_year
    centuary = year[0:2]
    num_year = year[2:]

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


alert = "IMPORTANT NOTE!"
alert = alert.center(40, "~")
thanks = "THANK YOU"
thanks = thanks.center(18, "~")
print("Welcome to DOOMSDAY! This is a program that tells you day of any date.")
imp_msg = "{0}\nIF YOU ENTER ANYTHING OTHER THAN INTEGERS CHARACTERS, THE PROGRAM WILL GIVE AN ERROR BECAUSE I HAVE NOT WRITTEN ANY ERROR HANDLING CODE. IF YOU ENTER IT BY MISTAKE THEN PLEASE RESTART THE PROGRAM\n{1}".format(alert, thanks)
imp_msg = imp_msg.rjust(20, " ")
print(imp_msg)
print("Give it a try!")
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
            again = "y"

        if str.lower(again) == "n":
            break
        else:
            #inputs
            date = int(input("Enter date: "))
            if type(date) != int:
                print("Please type an integer number in date!")
            month = int(input("Enter month: "))
            if type(month) != int:
                print("Please type an integer  in month!")
            year = int(input("Enter year: "))
            if type(year) != int:
                print("Please type an integer  in year!")
            
            #slice year
            year_split(year)

            #limit check
            date_limit(date) 
            month_limit(month)

            #check leap year
            lp_year(year)

            #febuary number of days check
            feb_limit(date, month)
            
        