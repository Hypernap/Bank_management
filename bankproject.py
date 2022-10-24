print("****WELCOME TO S.S BANK****")
print("****BANK TRANSACTION****")

from random import randint
import datetime
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="123456789")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists BANK")
mycursor.execute("use BANK")

mycursor.execute("create table if not exists bank_master(ACCOUNTNO varchar(12) primary key,NAME varchar(30),CITY char(20),MOBILENO char(10),BALANCE int(15))")
mycursor.execute("create table if not exists banktrans(ACCOUNTNO varchar (12),AMOUNT int(15),DATEOFTRANSCTION date,ttype char(10),remark varchar(50),foreign key (ACCOUNTNO) references bank_master(ACCOUNTNO))")
mydb.commit()
mycursor.execute("select ACCOUNTNO from bank_master")

w=[]

for t in mycursor:
    w.append(t)
mydb.commit()

while(True):
    
    print("1=Create account")
    print("2=Deposit money")
    print("3=Withdraw money")
    print("4=Display account")
    print("5=Account statment")
    print("6=Exit")
    ch=int(input("Enter your choice:"))
    

    if(ch==1):
        print("******************************")
        print("All information prompted are mandatory to be filled")
        print("******************************")
        i=0
        while i<1 :
            ACCOUNT=randint(1000,9999999)
            if ACCOUNT in w:
                i+=0
            else:
                i+=2
                w.append(ACCOUNT)
                ACCOUNTNO=str(ACCOUNT)+'SS01'
            
            
        print('YOUR ACCOUNT NUMBER GENERATED IS:',ACCOUNTNO)
        NAME=input("Enter NAME(limit 35 characters):")
        CITY=str(input("Enter CITY NAME:"))
        MOBIENO=str(input("Enter mobile no.:"))
        BALANCE=0
        mycursor.execute("insert into bank_master values('"+str(ACCOUNTNO)+"','"+NAME+"','"+CITY+"','"+MOBIENO+"','"+str(BALANCE)+"')")
        mydb.commit()
        print("******************************")
        print("Account is successfully created!!!")
        print("******************************")
    elif(ch==2):
        ACCOUNTNO=str(input("Enter account number:"))
        dp=int(input("Enter amount to be deposited:"))
        remark=input("Remark:")
        DATEOFTRANSCATION=datetime.datetime.now()
        ttype="Deposite"
        mycursor.execute("insert into banktrans values('"+ACCOUNTNO+"','"+str(dp)+"','"+str(DATEOFTRANSCATION)+"','"+ttype+"','"+str(remark)+"')")
        mycursor.execute("update bank_master set BALANCE=BALANCE+'"+str(dp)+"' where ACCOUNTNO='"+ACCOUNTNO+"'")
        mydb.commit()
        print("******************************")
        print("money has been deposited successully!!!")
        print("******************************")


    elif(ch==3):
        ACCOUNTNO=str(input("Enter account number:"))
        wd=int(input("Enter amount to be withdrawn:"))
        remark=input("Remark:")
        mycursor.execute("select BALANCE from bank_master where ACCOUNTNO='"+ACCOUNTNO+"'")
        for p in mycursor:
            for l in p:
                print("")
                
        if wd < l:
            DATEOFTRANSCATION=datetime.datetime.now()
            ttype="Withdrawal"
            remark=input("Remark:")
            mycursor.execute("insert into banktrans values('"+ACCOUNTNO+"','"+str(wd)+"','"+str(DATEOFTRANSCATION)+"','"+ttype+"','"+str(remark)+"')")
            mycursor.execute("update bank_master set BALANCE=BALANCE-'"+str(wd)+"' where ACCOUNTNO='"+ACCOUNTNO+"'")
            mydb.commit()
            print("******************************")
            print("money has been Withdrawal successully!!!")
            print("******************************")

        if wd > l:
            print("******************************")
            print('INSUFFICIENT BALANCE')
            print("******************************")
            pass
    elif(ch==4):
        ACCOUNTNO=str(input("Enter account number:"))
        mycursor.execute("select * from bank_master where ACCOUNTNO='"+ACCOUNTNO+"'")
        k=[]
        for i in mycursor:
            for j in i:
                k.append(j)
        print("******************************")
        print('ACCOUNT NUMBER IS',k[0])
        print('NAME OF ACCOUNT HOLDER IS',k[1])
        print('MOBILE NUMBER OF ACCOUNT HOLDER IS',k[3])
        print('RESIDENTIAL CITY OF ACCOUNT HOLDER IS',k[2])
        print('BALANCE IN THE ACCOUNT IS',k[4],' ₹')
        print("******************************")

    elif (ch==5):
        ACCOUNTNO=str(input("Enter account number:"))
        mycursor.execute("select * from banktrans where ACCOUNTNO='"+ACCOUNTNO+"'")
        amount=[]
        date=[]
        typ=[]
        remark=[]
        k=[]

        for i in mycursor:
            for j in i:
                k.append(j)

        for u in range(1,len(k),5):
            amount.append(k[u])

        for p in range(2,len(k),5):
            date.append(k[p])    

        for q in range(3,len(k),5):
            typ.append(k[q])

        for l in range(4,len(k),5):
            remark.append(k[l]) 

        mydb.commit
        mycursor.execute("select BALANCE from bank_master where ACCOUNTNO='"+ACCOUNTNO+"'")

        for b in mycursor:
            m=0
            for o in b:
                m+=o
            print("******************************")
            ctr=0
            bal=0

            while ctr < len(date):
                
                print(ctr+1,'AMOUNT TRANSCATED IS',amount[ctr])
                print('  TYPE OF TRANSCATION IS',typ[ctr])
                print('  DATE OF TRANSCTION IS',date[ctr])
                print('  REMARK',remark[ctr])
                
                if typ[ctr]=='Deposite':
                    bal+=amount[ctr]
                    print('  BALANCE',bal)
                else:
                    
                    bal=bal-amount[ctr]
                    print('  BALANCE',bal)
                ctr+=1
            print("******************************")

                    
    elif (ch==6):
        exit()

    else :
        print('******WRONG INPUT******')
        pass

    
        
