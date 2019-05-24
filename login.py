import sqlite3
from urllib.request import *
from bs4 import *
def login():
    a=sqlite3.connect("praveen.db")
    try:
          a.execute('drop table praveen')
          a.execute('create table praveen(username varchar(100),password varchar(100),mobile varchar(100))')
    except sqlite3.OperationalError:
        print("the table is already exit")
    a.commit()
    n=1
    while n==1:
        print("1.create account")
        print("2.login")
        print("3.forget or reset")
        b=int(input("enter ur choice"))
        if(b==1):
            try:
                a.execute('insert into praveen values(?,?,?)',(input("enter the your username"),input("enter the password"),input("enter the mobile number")))
            except ValueError:
                print("value error")
                a.commit()
                print("your account successfully created")
                n=2
        elif(b==2):
            try:
                n=(0,0)
                b=a.execute('select username,password from praveen where username=? and password=?',(input("enter the usename"),input("enter the password")))
                for n in b:
                    print("checking")
                if n[0]!=0 and n[1]!=0:
                    print("login Success")
                else:
                    print("invalid username or password")
            except ValueError:
                print("ValueError")
                a.commit()
                n=2
        elif(b==3):
            try:
                a.execute('update praveen set username=? where mobile=? and password=?',(input("enter the username"),input("enter the mobile"),input("enter the new password")))
            except ValueError:
                print("value Error")
                a.commit()
            print("Your password sucessfully reset")
            n=2
        else:
            exit(0)
        url="http://"+input('enter your url')
        z=(urlopen(url))
        a=BeautifulSoup(z,"html.parser")
        for y in a(["script","style"]):
            y.extract()
        b=a.get_text()
        b=b.split('\n')
        b=' '.join(b)
        z=open("given.txt","r")
        x=z.read()
        x=x.split(' ')
        m=b.split(' ')
        c=[ ]
        for i in m:
            if i not in c and i not in x:
                c.append(i)
                e=m.count(i)
        print(i,e)

login()
