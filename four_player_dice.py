import random

def first():
    while(1):
        x=int(input("enter any number  to roll your dice"))
        if (x==x):
            n=random.randint(1,6)
            if(n==1 or n==6):
                print("the value is---------->",n)
                print("do you have another chance to roll your dice")
                continue
            else:
                print("the value is---------->",n)
                break
        else:
            print("sorry you enter worng number,please enter again")
            continue


while(1):
    n=input("enter the any letter to start game")
    if(n==n):
        while(1):
            if(n==n):
                print("let start player 1")
                first()
                print("$"*25,"End of Player 1","$"*25)
                print("end of player 1 #####",end=" ")
                print("press any key to start the Game player 2" ,end=" ")
                a=input()
                if(a==a):
                    print("let start player 2")
                    first()
                    print("$"*25,"End of Player 2","$"*25)
                    print("end of player 2 ####",end=" ")
                    print("press any key to start the Game player 3",end=" ")
                    b=input("")
                    if(b==b):
                        print("let start player 3")
                        first()
                        print("$"*25,"End of Player 3","$"*25)
                        print("end of player 3####",end=" ")
                        print("press any key to start the Game player 4",end=" ")
                        c=input("")
                        if(c==c):
                            print("let start player 4")
                            first()
                            print("$"*25,"End of Player 4","$"*25)
                            print("end of player 4####",end=" ")
                            print("press any key to start the Game player 1",end=" ")
                n=input("")
                continue
            else:
                break

