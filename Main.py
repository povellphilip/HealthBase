import random,time,sys,tabulate,os

##Next letters appear in sequence
def typingprint(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.001)

##Loading screen
def loadingscreen(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.06)

##Next letters appear in sequence
def typinginput(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    value=input()
    return value

##To clear screen
def clearscreen():
    os.system("clear")

##To update values
def update(text):
     j=text
     mc=typinginput("ENTER THE NEW MEDICAL CONDITION:")
     md=typinginput("ENTER THE MEDICINES PRESCRIBED:")
     cur.execute(f"update patientile set Medicalcondition='{mc}' where Tokenno={j}")
     cur.execute(f"update patientile set Medicine='{md}' where Tokenno={j}")

##To insert values
def insertion():
    tn=int(typinginput("ENTER YOUR TOKEN NUMBER:"))
    n=typinginput("ENTER YOUR NAME:")
    d=typinginput("ENTER YOUR DOB [YYYY-MM-DD]:")
    mc=typinginput("ENTER YOUR MEDICAL CONDITION:")
    md=typinginput("ENTER THE MEDICINE PRESCRIBED:")
    #Add values to previously created Patient table
    cur.execute(f"insert into Patientile values({tn},'{n}','{d}','{mc}','{md}')")
    con.commit()

##To view values
def view():
        cur.execute("select * from Patientile")
        typingprint("\nTHE DETAILS OF THE PATIENT ARE:\n")
        d=cur.fetchall()
        print(tabulate.tabulate(d,tablefmt='grid',headers=['Token','Name','DOB','Medical condition','Medication'], numalign="center"))
             
##To delete values
def deletion(text):
        b=text
        cur.execute(f"delete from Patientile where Tokenno={b}")
        con.commit()
        typingprint("DETAILS OF PATIENT HAVE BEEN DELETED\n")

##To search for values
def srch(text):
        a=text
        cur.execute(f"select * from Patientile where Tokenno={a}")
        d=cur.fetchall()
        print(tabulate.tabulate(d,tablefmt='grid',headers=['Token','Name','DOB','Medical condition','Medication']))

##Forgot password
def forgot_password(text):
     j=text
     ps=typinginput("ENTER THE NEW PASSWORD:")
     cur.execute(f"update doctorate set password='{ps}' where username='{j}'")

     
import mysql.connector as mycon
con=mycon.connect(host='localhost',user='root',passwd='123')
cur=con.cursor()
##Create database
cur.execute("create database if not exists hosp")
cur.execute("use hosp")
##Create the table
cur.execute("create table if not exists Patientile(Tokenno int primary key, Name varchar(20), DOB date , Medicalcondition varchar(20), Medicine varchar(20))")
cur.execute('create table if not exists doctorate(username char(15),password char(10))')

##Main screen
while True:
     typingprint("\n****************************\n")
     typingprint("WELCOME TO THE NPRG HOSPITAL")
     typingprint("\n****************************\n")
     typingprint("[1] DOCTOR\n")
     typingprint("[2] PATIENT\n")
     typingprint("[3] ADMINISTRATOR\n")
     typingprint("[4] EXIT\n\n")
     try:
          n=int(typinginput("PLEASE SELECT YOUR CHOICE:"))
          if n==1:
            name=typinginput("ENTER YOUR USERNAME:")
            m=cur.execute(f"select password from doctorate where username ='{name}'")
            L= cur.fetchone()
            if L == None:
                 typingprint("USERNAME NOT FOUND")
            else:
                      passwordi=typinginput("PASSWORD:")
                      if passwordi==L[0]:
                           typingprint("ACCESS GRANTED\n")
                           while True:       
                               typingprint("\n1.VIEW THE DETAILS\n")
                               typingprint("2.DELETE THE DETAILS\n")
                               typingprint("3.SEARCH FOR A PATIENT\n")
                               typingprint("4.UPDATE THE DETAILS\n")
                               typingprint("5.EXIT\n")
                               choice=int(typinginput("ENTER YOUR CHOICE:"))
                               if choice==1:
                                   view()
                               elif choice==2:
                                    plus=typinginput("PLEASE ENTER A TOKEN NUMBER:")
                                    star=cur.execute(f"select * from patientile where tokenno ={plus}")
                                    num= cur.fetchone()
                                    if num == None:
                                        typingprint("USERNAME NOT FOUND")
                                    else:
                                        deletion(plus)
                                        view()
                                        
                               elif choice==3:
                                    namez=typinginput("PLEASE ENTER A TOKEN NUMBER:")
                                    mou=cur.execute(f"select * from patientile where tokenno ={namez}")
                                    j= cur.fetchone()
                                    if j == None:
                                        typingprint("USERNAME NOT FOUND")
                                    else:
                                         srch(namez)
                                         
                               elif choice==4:
                                     lim=typinginput("PLEASE ENTER A TOKEN NUMBER:")
                                     dou=cur.execute(f"select * from patientile where tokenno ={lim}")
                                     K= cur.fetchone()
                                     if K == None:
                                          typingprint("USERNAME NOT FOUND")
                                     else:
                                        update(lim)
                                        view()
                                        
                               elif choice==5:
                                   break
                      else:
                         typingprint("ACCESS DENIED")
                         continue

          elif n==2:
               while True:
                    typingprint("\n1.INSERT\n")
                    typingprint("2.PRINT RECEIPT\n")
                    typingprint("3.EXIT\n")
                    ch=int(typinginput("ENTER YOUR CHOICE:"))
                    if ch==1:
                       print( "YOUR TOKEN NUMBER IS:" ,random.randrange(99999))
                       insertion()
                       loadingscreen("LOADING.........")
                       typingprint("ROW INSERTED.\n")
                       
                    elif ch==3:
                       break
                    
                    elif ch==2:
                        import csv
                        f=open("patientprint.csv","w",newline='')
                        writers=csv.writer(f)
                        writers.writerow(["Name","Medicine"])
                        while True:
                            name=typinginput("ENTER YOUR NAME:")
                            medicine=typinginput("ENTER THE MEDICINE:")
                            writers.writerow([name,medicine])
                            ch=typinginput("DO YOU WANT TO CONTINUE (Y,N):")
                            
                            if ch=="n" or ch=="N":
                                break
                              
                        f.close()    
                        f=open("patientprint.csv","r")
                        reader=csv.reader(f)
                        for row in reader:
                            print(row)
                        f.close()
                        typingprint("DETAILS HAVE BEEN SAVED\n")
                       
          elif n==3:
            typingprint("\n1) ADD DOCTORS\n")
            typingprint("2) CHANGE PASSWORD\n")
            s=int(typinginput("ENTER YOUR CHOICE:"))
            if s==1:
               n=int(typinginput("ENTER NUMBER OF DOCTORS:"))
               for i in range(n):
                    username=typinginput("ENTER THE USERNAME TO BE ADDED:")
                    password=typinginput("ENTER THE PASSWORD OF THE DOCTOR:")
                    cur.execute(f"insert into doctorate values('{username}','{password}')")
                    con.commit()
            elif s==2:
                yiu=typinginput("PLEASE ENTER A DOCTOR NAME:")
                miga=cur.execute(f"select password from doctorate where username ='{yiu}'")
                num= cur.fetchone()
                if num == None:
                    typingprint("USERNAME NOT FOUND")
                else:
                    forgot_password(yiu)
                
          elif n==4:
               typingprint("\n**************************************\n")
               typingprint("THANK YOU FOR CHOOSING OUR HOSPITAL!!!")
               typingprint("\n**************************************\n")
               break
          else:
               typingprint("INVALID CHOICE, TRY AGAIN")
               continue
  
  ##Error Management
     except TypeError:
          typingprint("INVALID DATA TYPE, TRY AGAIN\n")
     except ValueError:
          typingprint("INVALID DATA TYPE,TRY AGAIN\n")
     except RuntimeError:
          typingprint("ERROR\n")
