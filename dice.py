import random

def first():
    while(1):
        x=int(input("enter any number  to roll your dice"))
        if (x==x):
            n=random.randint(1,6)
            if(n==1 or n==6):
                print(n)
                print("do you have another chance to roll your dice")
                continue
            else:
                print(n)
                break
        else:
            print("sorry you enter worng number,please enter again")
            continue

while(1):
    n=input("enter any letter to start the game:")
    if(n==n):
        print("let start to play")
        while(1):
            first()
            print("End of game for last player",end="")
            print("next player to start roll your dice")
            continue
    else:
        break
