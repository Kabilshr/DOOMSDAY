#while loop 
x = 0
while True:
    x+=1
    if x > 1:
        data = input("do you want to try again?y/n  ")
        if data == "n":
            break
    else:
        print("looping")
        print(x)