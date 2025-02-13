# enter age
#U2P2

num=int(input("Enter a Age ="))

if num < 12 :
    print("You are Kid")
else:
    if num < 12 or num < 17:
        print("You are Teenager")
    elif num < 18 or num < 60:
        print("You are Adult")
    else:
        print("You are Senior Citizen")
