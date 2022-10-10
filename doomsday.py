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
        if lp_year == True:
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



#tells if it is a leap year.
def lp_year(year):
    year = int(year)
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                lp_year = True
            else:
                lp_year = False
        else:
            lp_year = True
    else:
        lp_year = False

print("Welcome to DOOMSDAY! This is a program that tells you day of any date.\nGive it a try!")
while(True):
    date = eval(input("Enter date: "))
    if type(date) != int:
        print("Please type an integer number in date!")
    month = eval(input("Enter month: "))
    if type(month) != int:
        print("Please type an integer  in month!")
    year = eval(input("Enter year: "))
    if type(year) != int:
        print("Please type an integer  in year!")

    #limit check
    date_limit(date) 
    month_limit(month)

    #check leap year
    lp_year(year)

    #febuary number of days check
    feb_limit(date, month)

    