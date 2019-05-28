import sqlite3
import xlsxwriter
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
                    print()
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
                a.execute('update praveen set username=? where password=?  and mobile=?',(input("enter the username"),input("enter the new password"),input("enter the mobile number")))
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
         d={}
            for k in c:
                d[k]=e
        sort=sorted(d.items(),key=lambda t:t[1],reverse=False)
        wor=[]
        count=[]
        v=sort[0:5]
        xy=0
        for r in range(5):
            for y in range(1):
                wor.append(v[r][y])
                count.append(v[r][y+1])
    filename="praveen.xlsx"      
    workbook=xlsxwriter.Workbook(filename)                  
    worksheet=workbook.add_worksheet("Sheet1")
    worksheet.set_column(1,1,15)
    b= workbook.add_format({'bold': True})
    i= workbook.add_format({'italic': True})
    worksheet.write('A1', 'Words', b)
    worksheet.write('B1', 'Count', b)
    row=1
    col=0
    for i in range(5):
        worksheet.write(row,col,wor[i],i)
        worksheet.write_number(row,col+1, count[i])
        row+=1
    chart=workbook.add_chart({'type':'pie'})                 
    chart.add_series({'categories':'=Sheet1!$A$2:$A$6','values':'=Sheet1!$B$2:$B$6'})
    worksheet.insert_chart('G5',chart)


login()
