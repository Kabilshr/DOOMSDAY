
def limit(date, month):
    if date > 31:
        print("There can't be more than 31 days in a months.")
    else:
        return date
    if month > 12:
        print("There can't be more than 12 months.")
    else:
        return month



print("Welcome to DOOMSDAY! This is a program that tells you day of any date.\nGive it a try!")
while(True):
    date = eval(input("Enter date: "))
    print(type(date))
    if type(date) != int:
        print("Please type an integer number in date!")
    month = eval(input("Enter month: "))
    if type(month) != int:
        print("Please type an integer  in month!")
    year = eval(input("Enter year: "))
    if type(year) != int:
        print("Please type an integer  in year!")
    #limit check
    limit(date, month)