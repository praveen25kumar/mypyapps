import pyodbc
c=pyodbc.connect('Driver={SQL Server};'
                 'Server=10.200.2.118;'
                 'Database=AttuneMullti;'
                 'UID=sa;'
                 'PWD=Welcome123')
a = c.cursor()
s=input("enter the visitid")
b=a.execute('select  *  from AttuneMullti.dbo.patientvisit where Externalvisitid='+s)

n = [column[0] for column in b.description]
#print(columns)
for r in b:
    for i in range (len(n)):
        print(n[i]+ ':',r[i],end=" ")
        print("\n")

