'''num = input("enter number: ")
num = int(num)
tuesday = []
sunday = []
friday = []
wednesday = []
# tuesday
for A in range(00, 99, 4):
    tuesday.append(A)
# sunday
for B in range(1, 99, 4):
    sunday.append(B)
# friday
for C in range(2, 99, 4):
    friday.append(C)
# wednesday
for D in range(3, 99, 4):
    wednesday.append(D)

if num in tuesday:
    print("tuesday")
elif num in sunday:
    print("sunday")
elif num in friday:
    print("friday")
elif num in wednesday:
    print("wednesday")

'''
while True:
    x += 1
    print(x)
    if x == 2:
        break
    '''if x >1:
        data = input("do you want to try again?y/n  ")
        if data == "n":
            break
        else:
            continue
    else:
        print("looping")
        print(x)'''