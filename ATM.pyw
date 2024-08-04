from tkinter import *
import tkinter.messagebox as tmsg
from datetime import datetime, timedelta
import random
import string
from PIL import Image,ImageTk
import time
import pygame

def Create_account():
    root.withdraw()
    #Account Creation Window Starts from here
    root1=Toplevel(root)
    root1.geometry("1280x800")
    root1.minsize(1280,800)
    root1.maxsize(1280,800)
    root1.configure(bg="black")
    root1.wm_iconbitmap(r"assets\atmicon.ico")
    root1.title("Account Creation")
    
    def get_binary(x):
        binary_value="".join(format(ord(i),"08b") for i in x)
        return binary_value

    
    def update_clock():
        current_time = datetime.now().strftime("Date: %Y-%m-%d & Time: %H:%M:%S")
        label.config(text=current_time)
        label.after(1000, update_clock)
    
    def validate_input(new_value):
        return len(new_value) <= 11
    
    l=Label(root1,text=": Here Few Steps to Create Account :",bg="red",font="arial 28 bold")
    l.pack(fill=X)
    f=Frame(root1,bg="light blue")
    f.pack(fill=X)
    steps=["Step:1","Step:2","Step:3","Step:4","Step:5"]
    x=["Create Number","Personal Details","Pin Creation","Base-Deposit","Account Created"]
    for i in range(len(steps)):
        l1=Label(f,text=steps[i],font="arial 20 bold",bg="light blue")
        l1.grid(row=0,column=i,padx=80)
    for j in range(len(x)):
        l2=Label(f,text=x[j],font="arial 20 bold",bg="light blue")
        l2.grid(row=1,column=j,padx=20)
    sf=Frame(root1,bg="black")
    sf.pack()
    Label(sf,text="",font="arial 28 bold",bg="black").pack()
    space1=Label(sf,text="Create Account & Fill Personal Details",font="arial 28 bold",bg="yellow")
    space1.pack(anchor="center")
    Label(sf,text="",font="arial 28 bold",bg="black").pack()
    f1=Frame(root1,bg="black")
    f1.pack(fill=X)
    
    def button_1():
        Accn=accn.get()
        if len(Accn)!=11 or Accn.isdigit()==False:
            val=tmsg.askokcancel("Status","Please Enter A Valid Account Number")
            if val==FALSE:
                root1.destroy()
                root.deiconify()
            else:
                var.set("")
        elif Accn:
            Accn=get_binary(Accn)
            with open("ATM.txt","r") as f:
                data=f.readlines()
                for i in data:
                    if i.startswith("Account Number: "+Accn) or Accn=="0011000000110000001100000011000000110000001100000011000000110000001100000011000000110000":
                        val=tmsg.askokcancel("Status","Account Number is Already Present!.....Please Try With Different Account Number..")
                        if  val==True:
                            var.set("")
                        else:
                            root1.destroy()
                            root.deiconify()
                        break
                else:
                    tmsg.askokcancel("Status","Account Number Added Successfully.....")
    def button_2():
        Name=n.get()
        Name=Name.capitalize()
        if Name.isalpha()==False:
            val=tmsg.askokcancel("Status","First Name Should Contain Characters Only!....")
            if val==FALSE:
                root1.destroy()
                root.deiconify()
            else:
                var1.set("")
        else:
            tmsg.askokcancel("Status","First Name Added Successfully.....")
    def button_3():
        L_Name=sn.get()
        L_Name=L_Name.capitalize()
        if L_Name.isalpha()==False:
            val=tmsg.askokcancel("Status","Last Name Should Contain Characters Only!....")
            if val==FALSE:
                root1.destroy()
                root.deiconify()
            else:
                var2.set("")
        else:
            tmsg.askokcancel("Status","Last Name Added Successfully.....") 
    def button_4():
        if len(g.get())==0:
            tmsg.askokcancel("Status","Please Add Gender.....")
        else:
            Gender = g.get()
            if Gender.startswith("M") or Gender.startswith("m"):
                Gender="Male"
                tmsg.askokcancel("Status","Gender Added Successfully.....")
            elif Gender.startswith("f") or Gender.startswith("F"):
                Gender="Female"
                tmsg.askokcancel("Status","Gender Added Successfully.....")
            else:
                Gender = g.get()
                tmsg.askokcancel("Status","Gender Added Successfully.....")
    def button_5():
        if len(dob.get())==0:
            tmsg.askokcancel("Status","Please Add Date Of Birth.....")
        else:
            DOB=dob.get()
            if "/" in DOB:
                date,month,year=DOB.split("/")
            elif "." in DOB:
                date,month,year=DOB.split(".")
            elif "-" in DOB:
                date,month,year=DOB.split("-")
            elif "|" in DOB:
                date,month,year=DOB.split("|")
            if len(date)==1:
                date="0"+date
            d=int(date)
            if d>31:
                val=tmsg.askokcancel("Status","Date Should be Less than or Equal to 31")
                if val==True:
                    var4.set("")
                else:
                    root1.destroy()
                    root.deiconify()
            else:
                if len(month)==1:
                    month="0"+month
                m=int(month)
                if m>12:
                    val=tmsg.askokcancel("Status","Month Should be Less than or Equal to 12")
                    if val==True:
                        var4.set("")
                    else:
                        root1.destroy()
                        root.deiconify()
                elif m==2 and d>29:
                    val=tmsg.askokcancel("Status","In February Month Date Should be Less than or Equal to 29!")
                    if val==True:
                        var4.set("") 
                    else:
                        root.destroy()
                        root.deiconify()   
                else:
                    y=int(year)
                    Y=datetime.now()
                    if y<1950 or y>Y.year:
                        val=tmsg.askokcancel("Status","Please Enter A Valid Year")
                        if val==True:
                            var4.set("")
                        else:
                            root1.destroy()
                            root.deiconify()
                    else:
                        val=tmsg.askokcancel("Status","Date Of Birth Added Successfully")
    
    def final_sub():
        Accn=accn.get()
        if len(Accn)!=11 or Accn.isdigit()==False:
            val=tmsg.askokcancel("Status","Please Enter A Valid Account Number")
            if val==FALSE:
                root1.destroy()
                root.deiconify()
            else:
                var.set("")
        elif Accn:
            Accn=get_binary(Accn)
            with open("ATM.txt","r") as f:
                data=f.readlines()
                for i in data:
                    if i.startswith("Account Number: "+Accn) or Accn=="0011000000110000001100000011000000110000001100000011000000110000001100000011000000110000":
                        val=tmsg.askokcancel("Status","Account Number is Already Present!.....Please Try With Different Account Number..")
                        if val==True:
                            var.set("")
                        else:
                            root1.destroy()
                            root.deiconify()
                        break
                else:
                    Name=n.get()
                    Name=Name.capitalize()
                    if Name.isalpha()==False:
                        val=tmsg.askokcancel("Status","First Name Should Contain Characters Only!....")
                        if val==FALSE:
                            root1.destroy()
                            root.deiconify()
                        else:
                            var1.set("")
                    else:
                        L_Name=sn.get()
                        L_Name=L_Name.capitalize()
                        if L_Name.isalpha()==False:
                            val=tmsg.askokcancel("Status","Last Name Should Contain Characters Only!....")
                            if val==FALSE:
                                root1.destroy()
                                root.deiconify()
                            else:
                                var2.set("")
                        else:
                            if len(g.get())==0:
                                tmsg.askokcancel("Status","Please Enter Gender...")
                            else:
                                Gender = g.get()
                                if Gender.startswith("M") or Gender.startswith("m"):
                                    Gender="Male"
                                elif Gender.startswith("f") or Gender.startswith("F"):
                                    Gender="Female"
                                else:
                                    Gender = g.get()
                                if len(dob.get())==0:
                                    tmsg.askokcancel("Status","Please Enter Date Of Birth...")
                                else:
                                    DOB=dob.get()
                                    if "/" in DOB:
                                        date,month,year=DOB.split("/")
                                    elif "." in DOB:
                                        date,month,year=DOB.split(".")
                                    elif "-" in DOB:
                                        date,month,year=DOB.split("-")
                                    elif "|" in DOB:
                                        date,month,year=DOB.split("|")
                                    if len(date)==1:
                                        date="0"+date
                                    d=int(date)
                                    if d>31:
                                        val=tmsg.askokcancel("Status","Date Should be Less than or Equal to 31")
                                        if val==True:
                                            var4.set("")
                                        else:
                                            root1.destroy()
                                            root.deiconify()
                                    else:
                                        if len(month)==1:
                                            month="0"+month
                                        m=int(month)
                                        if m>12:
                                            val=tmsg.askokcancel("Status","Month Should be Less than or Equal to 12")
                                            if val==True:
                                                var4.set("")
                                            else:
                                                root1.destroy()
                                                root.deiconify()
                                        elif m==2 and d>29:
                                            val=tmsg.askokcancel("Status","In February Month Date Should be Less than or Equal to 29!") 
                                            if val==True:
                                                var4.set("") 
                                            else:
                                                root1.destroy()
                                                root.deiconify()
                                        else:
                                            y=int(year)
                                            Y=datetime.now()
                                            if y<1950 or y>Y.year:
                                                val=tmsg.askokcancel("Status","Please Enter A Valid Year")
                                                if val==True:
                                                    var4.set("")
                                                else:
                                                    root1.destroy()
                                                    root.deiconify()
                                            else:
                                                bday=year+"-"+month+"-"+date
                                                birthday=datetime.strptime(bday,"%Y-%m-%d")
                                                today=datetime.now()
                                                age=today.year-birthday.year-((today.month,today.day)<(birthday.month,birthday.day))
                                                tmsg.askokcancel("Status","Details Added Successfully.....")
                                                Name=get_binary(Name)
                                                L_Name=get_binary(L_Name)
                                                age=get_binary(str(age))
                                                Gender=get_binary(Gender)
                                                with open("ATM.txt","a") as file:
                                                    file.write(f"Account Number: {Accn}; Customer Name: {Name} {L_Name}; Age: {age}; Gender: {Gender};")
                                                submit.config(state="disabled")
                                                nxt.config(state=NORMAL)
                                
    l=Label(f1,text="1.Set An Account Number of 11 Digits : ",bg="black",font="arial 20 bold",fg="white")
    l.grid(row=0,column=0,pady=5)
    var=StringVar()
    accn=Entry(f1,textvariable=var,font="arial 30 bold",relief="sunken",width=30,justify="center",validate="key", validatecommand=(root.register(validate_input), "%P"))
    accn.grid(row=0,column=1,pady=5)
    add1=Button(f1,text="Add",bg="green",font="arial 16 bold",fg="White",relief="raised",command=button_1)
    add1.grid(row=0,column=2,pady=5,padx=10)
    
    name=Label(f1,text="2.Enter First Name : ",bg="black",fg="white",font="arial 20 bold")
    name.grid(row=1,column=0,pady=5)
    var1=StringVar()
    n=Entry(f1,textvariable=var1,font="arial 30 bold",relief="sunken",width=30,justify="center")
    n.grid(row=1,column=1,pady=5)
    add2=Button(f1,text="Add",bg="green",font="arial 16 bold",fg="White",relief="raised",command=button_2)
    add2.grid(row=1,column=2,pady=5,padx=10)
    
    sname=Label(f1,text="3.Enter Last Name : ",bg="black",fg="white",font="arial 20 bold")
    sname.grid(row=2,column=0,pady=5)
    var2=StringVar()
    sn=Entry(f1,textvariable=var2,font="arial 30 bold",relief="sunken",width=30,justify="center")
    sn.grid(row=2,column=1,pady=5)
    add3=Button(f1,text="Add",bg="green",font="arial 16 bold",fg="White",relief="raised",command=button_3)
    add3.grid(row=2,column=2,pady=5,padx=10)
    
    gender=Label(f1,text="4.Enter Gender : ",bg="black",fg="white",font="arial 20 bold")
    gender.grid(row=3,column=0,pady=5)
    var3=StringVar()
    g=Entry(f1,textvariable=var3,font="arial 30 bold",relief="sunken",width=30,justify="center")
    g.grid(row=3,column=1,pady=5)
    add4=Button(f1,text="Add",bg="green",font="arial 16 bold",fg="White",relief="raised",command=button_4)
    add4.grid(row=3,column=2,pady=5,padx=10)
    
    Dob=Label(f1,text="5.Enter DOB in (dd/mm/yyyy) Format : ",bg="black",fg="white",font="arial 20 bold")
    Dob.grid(row=4,column=0,pady=5)
    var4=StringVar()
    dob=Entry(f1,textvariable=var4,font="arial 30 bold",relief="sunken",width=30,justify="center")
    dob.grid(row=4,column=1,pady=5)
    add5=Button(f1,text="Add",bg="green",font="arial 16 bold",fg="White",relief="raised",command=button_5)
    add5.grid(row=4,column=2,pady=5,padx=10)

    submit=Button(f1,text="Save",font="arial 24 bold",bg="blue",fg="white",relief="raised",command=final_sub,padx=30)
    submit.grid(row=5,column=1,pady=5)
    
    def Next():
        def get_binary(x):
            binary_value="".join(format(ord(i),"08b") for i in x)
            return binary_value
        
        if len(accn.get())==0 or len(n.get())==0 or len(sn.get())==0 or len(g.get())==0 or len(dob.get())==0:
            x=tmsg.askokcancel("Status","Please Fill All The Entries!...")
        else:
            Accn=get_binary(accn.get())
            with open("ATM.txt","r") as file:
                data=file.readlines()
                for i in data:
                    if i.startswith("Account Number: "+Accn):
                        root1.withdraw()
                        #Pin Creation Window starts from here
                        root2=Toplevel(root1)
                        root2.geometry("1280x800")
                        root2.minsize(1280,800)
                        root2.maxsize(1280,800)
                        root2.configure(bg="aqua")
                        root2.wm_iconbitmap(r"assets\atmicon.ico")
                        root2.title("Account Creation")
                        
                        def get_binary(x):
                            binary_value="".join(format(ord(i),"08b") for i in x)
                            return binary_value

                        def decode(x):
                            original_data=" ".join(x[i:i+8] for i in range(0,len(x),8))
                            data=original_data.split()
                            decimal_value= ''.join(chr(int(i, 2)) for i in data)
                            return decimal_value
                        
                        def update_clock():
                            current_time = datetime.now().strftime("Date: %Y-%m-%d & Time: %H:%M:%S")
                            label.config(text=current_time)
                            label.after(1000, update_clock)
                        
                        def validate_input(new_value):
                            return len(new_value) <= 4
                        
                        def val_in(new_value):
                            return len(new_value) <= 10
                        
                        Label(root2,text="Create Your 4 digit Pin/Secret Number",font="arial 28 bold",bg="yellow").pack(fill=X)
                        Label(root2,text="",font="arial 20 bold",bg="aqua").pack(fill=X)
                        
                        of=Frame(root2,bg="black",relief="solid",borderwidth=4)
                        of.pack()
                        f=Frame(of,bg="yellow",relief="solid",borderwidth=4)
                        f.pack()
                        
                        def a1():
                            if len(p1.get())==4 and p1.get().isdigit()==True:
                                tmsg.askokcancel("Status","Successfully Added Pin Choice 1")
                            else:
                                x1=tmsg.askokcancel("Status","Pin Should be of 4 Numeric Digits without Consisting Any Characters")
                                if x1==False:
                                    var1.set("")
                                else:
                                    var1.set("")
                        
                        def a2():
                            if len(p2.get())==4 and p2.get().isdigit()==True:
                                tmsg.askokcancel("Status","Successfully Added Pin Choice 2")
                            else:
                                x2=tmsg.askokcancel("Status","Pin Should be of 4 Numeric Digits without Consisting Any Characters")
                                if x2==False:
                                    var2.set("")
                                else:
                                    var2.set("")
                        
                        def a3():
                            if len(p3.get())==4 and p3.get().isdigit()==True:
                                tmsg.askokcancel("Status","Successfully Added Pin Choice 3")
                            else:
                                x3=tmsg.askokcancel("Status","Pin Should be of 4 Numeric Digits without Consisting Any Characters")
                                if x3==False:
                                    var3.set("")
                                else:
                                    var3.set("")
                                    
                        var1=StringVar()
                        Label(f,text=f"Enter 4 digit Pin Choice: 1",font="arial 20 bold",bg="yellow",fg="black").grid(row=0,column=0,padx=10,pady=5)
                        p1=Entry(f,textvariable=var1,font="arial 30 bold",relief="sunken",width=20,justify="center",validate="key", validatecommand=(root.register(validate_input), "%P"))
                        p1.grid(row=0,column=1,padx=10,pady=5)
                        ad1=Button(f,text="Add",bg="green",font="arial 16 bold",fg="White",relief="raised",command=a1)
                        ad1.grid(row=0,column=2,padx=10,pady=5)
                        
                        var2=StringVar()
                        Label(f,text=f"Enter 4 digit Pin Choice: 2",font="arial 20 bold",bg="yellow",fg="black").grid(row=1,column=0,padx=10,pady=5)
                        p2=Entry(f,textvariable=var2,font="arial 30 bold",relief="sunken",width=20,justify="center",validate="key", validatecommand=(root.register(validate_input), "%P"))
                        p2.grid(row=1,column=1,padx=10,pady=5)
                        ad2=Button(f,text="Add",bg="green",font="arial 16 bold",fg="White",relief="raised",command=a2)
                        ad2.grid(row=1,column=2,padx=10,pady=5)
                        
                        var3=StringVar()
                        Label(f,text=f"Enter 4 digit Pin Choice: 3",font="arial 20 bold",bg="yellow",fg="black").grid(row=2,column=0,padx=10,pady=5)
                        p3=Entry(f,textvariable=var3,font="arial 30 bold",relief="sunken",width=20,justify="center",validate="key", validatecommand=(root.register(validate_input), "%P"))
                        p3.grid(row=2,column=1,padx=10,pady=5)
                        ad3=Button(f,text="Add",bg="green",font="arial 16 bold",fg="White",relief="raised",command=a3)
                        ad3.grid(row=2,column=2,padx=10,pady=5)
                        v=StringVar()
                        with open("ATM.txt","r") as f:
                            data=f.readlines()
                            for i in data:
                                if i.startswith("Account Number: "+Accn):
                                    x,y=i.split("Age: ")
                                    old,z=y.split("; Gender: ")
                            old=decode(old)
                            if int(old)<18:
                                st="disabled"
                                v.set("Minor Account")
                            else:
                                st="normal"
                        if int(old)<18:
                            Label(of,text="Deposit not Requiered for Under Age Customer",font="arial 28 bold",bg="red",fg="black").pack(pady=5,fill=X)
                        else:
                            Label(of,text="Enter The Amount(= or > Rs-2000) to Deposit:",font="arial 28 bold",bg="red",fg="black").pack(pady=5,fill=X)
                        f1=Frame(of,bg="black",relief="solid",borderwidth=4)
                        f1.pack()
                        
                        def a4():
                            if len(cont.get())==0:
                                tmsg.askokcancel("Status","Please Enter The Contact Number....")
                            elif len(cont.get())!=10 or cont.get().isdigit()==False:
                                y2=tmsg.askokcancel("Status","Please Enter A Valid Contact Number....")
                                if y2==False:
                                    v1.set("")
                                else:
                                    v1.set("")
                            else:
                                tmsg.askokcancel("Status","Successfully Added Contact Number....")
                        
                        def a5():
                            if len(amount.get())==0:
                                y1=tmsg.askokcancel("Status","Please Enter The Amount....")
                                if y1==False:
                                    v.set("")
                                else:
                                    v.set("")
                            elif amount.get().isdigit()==False and amount.get()!="Minor Account":
                                y3=tmsg.askokcancel("Status","Please Enter A Valid Amount....")
                                if y3==False:
                                    v.set("")
                                else:
                                    v.set("")
                            elif int(amount.get())==0 or int(amount.get()) <0:
                                y5=tmsg.askokcancel("Status","Please Enter A Valid Amount....")
                                if y5==False:
                                    v.set("")
                                else:
                                    v.set("")
                            else:
                                tmsg.askokcancel("Status","Successfully Added Amount....")
                        
                        Label(f1,text="Add Contact Number ->",font="arial 20 bold",bg="black",fg="white").grid(row=0,column=0,padx=5)
                        v1=StringVar()
                        cont=Entry(f1,textvariable=v1,font="arial 30 bold",relief="sunken",width=20,justify="center", validate="key", validatecommand=(root.register(val_in), "%P"))
                        cont.grid(row=0,column=1,pady=5)
                        ad4=Button(f1,text="Add",bg="green",font="arial 16 bold",fg="White",relief="raised",command=a4)
                        ad4.grid(row=0,column=2,padx=10,pady=5)
                        Label(f1,text="Add Amount Here ->",font="arial 20 bold",bg="black",fg="white").grid(row=1,column=0,padx=5)
                        amount=Entry(f1,textvariable=v,font="arial 30 bold",relief="sunken",width=20,justify="center",state=st)
                        amount.grid(row=1,column=1,pady=5)
                        ad5=Button(f1,text="Add",bg="green",font="arial 16 bold",fg="White",relief="raised",command=a5,state=st)
                        ad5.grid(row=1,column=2,padx=10,pady=5)
                        
                        def create():
                            if len(p1.get())==0 or len(p2.get())==0 or len(p3.get())==0:
                                tmsg.askokcancel("Status","Please Fill All PIN Choices....")
                            elif len(p1.get())!=4 or p1.get().isdigit()==False or len(p2.get())!=4 or p2.get().isdigit()==False or len(p3.get())!=4 or p3.get().isdigit()==False:
                                y1=tmsg.askokcancel("Status","Pin Should be of 4 Numeric Digits without Consisting Any Characters")
                                if y1==False:
                                    if len(p1.get())!=4 or p1.get().isdigit()==False:
                                        var1.set("")
                                    elif len(p2.get())!=4 or p2.get().isdigit()==False:
                                        var2.set("")
                                    elif len(p3.get())!=4 or p3.get().isdigit()==False:
                                        var3.set("")
                                else:
                                    if len(p1.get())!=4 or p1.get().isdigit()==False:
                                        var1.set("")
                                    elif len(p2.get())!=4 or p2.get().isdigit()==False:
                                        var2.set("")
                                    elif len(p3.get())!=4 or p3.get().isdigit()==False:
                                        var3.set("")
                            elif len(cont.get())==0:
                                tmsg.askokcancel("Status","Please Enter The Contact Number....")
                            elif len(cont.get())!=10 or cont.get().isdigit()==False:
                                y2=tmsg.askokcancel("Status","Please Enter A Valid Contact Number....")
                                if y2==False:
                                    v1.set("")
                                else:
                                    v1.set("")
                            elif len(amount.get())==0:
                                y1=tmsg.askokcancel("Status","Please Enter The Amount....")
                                if y1==False:
                                    v.set("")
                                else:
                                    v.set("")
                            elif amount.get().isdigit()==False and amount.get()!="Minor Account":
                                y3=tmsg.askokcancel("Status","Please Enter A Valid Amount....")
                                if y3==False:
                                    v.set("")
                                else:
                                    v.set("")
                            else:
                                pin=(p1.get(),p2.get(),p3.get())
                                with open("ATM.txt","r") as f:
                                    data=f.readlines()
                                    for i in data:
                                        if i.startswith("Account Number: "+Accn):
                                            x,y=i.split("Age: ")
                                            old,z=y.split("; Gender: ")
                                    old=decode(old)
                                    if int(old)<18:
                                        mage="(Minor Account)"
                                    else:
                                        mage=""
                                    sys_pin=random.choice(pin)
                                    if int(old)<18: 
                                        s=tmsg.askokcancel("Status","Congratulations!...Account Created Successfully....")
                                        cn=get_binary(cont.get())
                                        sys_pin=get_binary(sys_pin)
                                        x="0"
                                        x=get_binary(x)
                                        mage=get_binary(mage)
                                        if s==True:
                                            with open("ATM.txt","a") as file:
                                                file.write(f" Contact Number: {cn}; PIN: {sys_pin}; Balance: {x};{mage}\n")
                                            with open("ATM.txt","r") as f:
                                                data=f.readlines()
                                                for i in data:
                                                    if i.startswith("Account Number: "+Accn):
                                                        i=i[len("Account Number: "):]
                                                        Ano,b=i.split("; Customer Name: ")
                                                        Ano=decode(Ano)
                                                        name,c=b.split("; Age: ")
                                                        n1,n2=name.split(" ")
                                                        n1=decode(n1)
                                                        n2=decode(n2)
                                                        name=n1+" "+n2
                                                        age,d=c.split("; Gender: ")
                                                        age=decode(age)
                                                        gen,e=d.split("; Contact Number: ")
                                                        gen=decode(gen)
                                                        contact,f=e.split("; PIN: ")
                                                        contact=decode(contact)
                                                        Pin,g=f.split("; Balance: ")
                                                        Pin=decode(Pin)
                                                        
                                                tmsg.askokcancel("Account Details",f"Account Number: {Ano}; Account Holder Name: {name}; Age: {age}; Gender: {gen}; Contact Number: {contact}; PIN: {Pin}; Balance: 0; Account Type: {decode(mage)}") #It's because This line is outside of the loop so it will take the last values of the loop
                                                nxt1.config(state=NORMAL)
                                                prev1.config(state=DISABLED)
                                                cb.config(state=DISABLED)
                                        else:
                                            with open("ATM.txt","a") as file:
                                                file.write(f" Contact Number: {cn}; PIN: {sys_pin}; Balance: {x};{mage}\n")
                                                nxt1.config(state=NORMAL)
                                                prev1.config(state=DISABLED)
                                                cb.config(state=DISABLED)
                                    elif int(amount.get())>=2000:
                                        s=tmsg.askokcancel("Status","Congratulations!...Account Created Successfully....")
                                        cn=get_binary(cont.get())
                                        sys_pin=get_binary(sys_pin)
                                        x=amount.get()
                                        x=get_binary(x)
                                        mage=get_binary(mage)
                                        if s==True:
                                            with open("ATM.txt","a") as file:
                                                file.write(f" Contact Number: {cn}; PIN: {sys_pin}; Balance: {x};{mage}\n")
                                            with open("ATM.txt","r") as f:
                                                data=f.readlines()
                                                for i in data:
                                                    if i.startswith("Account Number: "+Accn):
                                                        i=i[len("Account Number: "):]
                                                        Ano,b=i.split("; Customer Name: ")
                                                        Ano=decode(Ano)
                                                        name,c=b.split("; Age: ")
                                                        n1,n2=name.split(" ")
                                                        n1=decode(n1)
                                                        n2=decode(n2)
                                                        name=n1+" "+n2
                                                        age,d=c.split("; Gender: ")
                                                        age=decode(age)
                                                        gen,e=d.split("; Contact Number: ")
                                                        gen=decode(gen)
                                                        contact,f=e.split("; PIN: ")
                                                        contact=decode(contact)
                                                        Pin,g=f.split("; Balance: ")
                                                        Pin=decode(Pin)
                                                        bal,ext=g.split(";")
                                                        bal=decode(bal)
                                                        
                                                tmsg.askokcancel("Account Details",f"Account Number: {Ano}; Account Holder Name: {name}; Age: {age}; Gender: {gen};Contact Number: {contact}; PIN: {Pin}; Balance: {bal}") #It's because This line is outside of the loop so it will take the last values of the loop
                                                nxt1.config(state=NORMAL)
                                                prev1.config(state=DISABLED)
                                                cb.config(state=DISABLED)
                                        else:
                                            with open("ATM.txt","a") as file:
                                                file.write(f" Contact Number: {cn}; PIN: {sys_pin}; Balance: {x};{mage}\n")
                                                nxt1.config(state=NORMAL)
                                                prev1.config(state=DISABLED)
                                                cb.config(state=DISABLED)
                                    else:
                                        y2=tmsg.askokcancel("Status","Deposit Amount Should be Gretter than or Equal to Rs-2000")
                                        if y2==False:
                                            v.set("")
                                        else:
                                            v.set("")
                        
                        cb=Button(of,text="Create Account",bg="blue",fg="white",relief="raised",font="arial 20 bold",command=create,state=NORMAL)
                        cb.pack(pady=5)
                        Label(root2,text="",font="arial 20 bold",bg="aqua").pack(pady=38)
                        
                        
                        f5=Frame(root2,bg="aqua")
                        f5.pack()
                        
                        def previous1():
                            # if len(p1.get())!=4 or p1.get().isdigit()==False or len(p2.get())!=4 or p2.get().isdigit()==False or len(p3.get())!=4 or p3.get().isdigit()==False or len(amount.get())==0 or len(amount.get())!=0 or amount.get()=="Minor Account" or int(amount.get())<2000:
                            with open("ATM.txt","r") as f:
                                    data=f.readlines()[:-1]
                                    f.seek(0)
                            with open("ATM.txt","w") as file:
                                    file.writelines(data)
                                    
                            root2.destroy()
                            root1.deiconify()
                            submit.config(state="normal")
                        def next1():
                            root2.destroy()
                            root.deiconify()
                        prev1=Button(f5,text="<<Previous",bg="green",font="arial 14 bold",fg="White",relief="raised",command=previous1,state=NORMAL)
                        prev1.grid(row=0,column=0)
                        Label(f5,text="",font="arial 14 bold",bg="aqua").grid(row=0,column=1,padx=535)
                        nxt1=Button(f5,text="Next>>",bg="green",font="arial 14 bold",fg="White",relief="raised",command=next1,state=DISABLED)
                        nxt1.grid(row=0,column=2)
                        status_bar=Frame(root2)
                        status_bar.pack(fill=X)
                        label=Label(status_bar,fg="blue",font="arial 20 bold",bg="yellow")
                        label.pack(fill=X)
                        update_clock()
                        root2.mainloop()
                        break
                else:
                    tmsg.askokcancel("Status","Please Save The Details....")
    
    def Previous():
        if accn.get() or n.get() or sn.get() or g.get() or dob.get():
            with open("ATM.txt","r+") as f:
                history=f.readlines()
                Accn=get_binary(accn.get())
                for i in history:
                    if i.startswith("Account Number: "+Accn):
                        f.seek(0)
                        f.truncate()
                        f.writelines(history[:-1])       
        root1.destroy()  # Destroy the new window
        root.deiconify()  # Restore the main window
    f4=Frame(root1,bg="black")
    f4.pack(fill=X)
    prev=Button(f4,text="<<Previous",bg="green",font="arial 14 bold",fg="White",relief="raised",command=Previous)
    prev.grid(row=0,column=0)
    Label(f4,text="",font="arial 14 bold",bg="black").grid(row=0,column=1,padx=535)
    nxt=Button(f4,text="Next>>",bg="green",font="arial 14 bold",fg="White",relief="raised",command=Next,state=DISABLED)
    nxt.grid(row=0,column=2)
    
    status_bar=Frame(root1)
    status_bar.pack(fill=X)
    label=Label(status_bar,fg="blue",font="arial 20 bold",bg="yellow")
    label.pack(fill=X)
    update_clock()
    root1.mainloop()

def get_account():
    root.withdraw()
    new_root=Toplevel(root)
    new_root.geometry("1280x800")
    new_root.minsize(1280,800)
    new_root.maxsize(1280,800)
    new_root.wm_iconbitmap(r"assets\atmicon.ico")
    new_root.title("ATM MACHINE")
    
    image=Image.open(r"assets\a.jpg")
    photo=ImageTk.PhotoImage(image)
    
    background_label =Label(new_root, image=photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    
    def update_clock():
        current_time = datetime.now().strftime("Date: %Y-%m-%d & Time: %H:%M:%S")
        label.config(text=current_time)
        label.after(1000, update_clock)
    def validate_input(new_value):
        return len(new_value) <= 11
    
    def details():
        if len(a_num.get())==0:
            tmsg.askokcancel("Status","Please Enter The Account Number...")
        else:
            Accn=a_num.get()
            if len(Accn)!=11 or Accn.isdigit()==False:
                val=tmsg.askokcancel("Status","Please Enter A Valid Account Number")
                if val==FALSE:
                    new_root.destroy()
                    root.deiconify()
                else:
                    var.set("")
            else:
                with open("ATM.txt","r") as file:
                        data=file.readlines()
                        if len(data)==0 and Accn!="00000000000":
                            tmsg.askokcancel("Status","You Don't Have any Account! Please Create an Account...")
                            new_root.destroy()
                            root.deiconify()
                        else:
                            def get_binary(x):
                                binary_value="".join(format(ord(i),"08b") for i in x)
                                return binary_value
                            
                            def decode(x):
                                original_data=" ".join(x[i:i+8] for i in range(0,len(x),8))
                                data=original_data.split()
                                decimal_value= ''.join(chr(int(i, 2)) for i in data)
                                return decimal_value

                            Ac=a_num.get()
                            Ac=get_binary(Ac)
                            with open("ATM.txt","r") as file:
                                data=file.readlines()
                                # for i in data:
                                if any(i.startswith("Account Number: "+Ac)for i in data) or Ac=="0011000000110000001100000011000000110000001100000011000000110000001100000011000000110000":#IT is the binary form of 00000000000
                                #any(i.startswith("Account Number: "+Ac) for i in data): This part of the expression checks if any line in the data list starts with the string "Account Number: " concatenated with the value of Ac. If any line in data meets this condition, any() returns True, otherwise it returns False.
                                #Ac=="00000000000": This part of the expression checks if the value of Ac is equal to "00000000000". If Ac is equal to this string, the condition evaluates to True, otherwise it evaluates to False.
                                #The or operator is used to combine these two conditions. If either of them is True, the entire expression evaluates to True. Otherwise, if both are False, the entire expression evaluates to False.    
                                        new_root.withdraw()
                                        new_root2=Toplevel(new_root)
                                        new_root2.geometry("1280x800")
                                        new_root2.minsize(1280,800)
                                        new_root2.maxsize(1280,800)
                                        new_root2.configure(bg="lavender")
                                        new_root2.wm_iconbitmap(r"assets\atmicon.ico")
                                        new_root2.title("ATM MACHINE OPERATION")
                                        
                                        def hide_message_box():
                                            new_root.destroy()
                                            new_root2.destroy()
                                            root.deiconify()
                                            tmsg.askokcancel("Status","Session Time Out...")
                                        
                                        def update_clock():
                                            current_time = datetime.now().strftime("Date: %Y-%m-%d & Time: %H:%M:%S")
                                            label.config(text=current_time)
                                            label.after(1000, update_clock)
                                        
                                        f=Frame(new_root2,bg="red")
                                        f.pack(fill=X)
                                        Label(f,text="Operation Panel",bg="red",fg="white",font="arial 28 bold").pack()
                                        Label(f,text="",bg="lavender",font="arial 28 bold").pack(fill=X)
                                        
                                        f1=Frame(new_root2,bg="lavender")
                                        f1.pack(fill=X)
                                        if a_num.get()=="00000000000":
                                            st=NORMAL
                                            s=DISABLED
                                        else:
                                            st=DISABLED
                                            s=NORMAL
                                            
                                        def balance():
                                            with open("ATM.txt","r") as f:
                                                data=f.readlines()
                                                for i in data:
                                                    if i.startswith("Account Number: "+Ac):
                                                        x,y=i.split("Customer Name: ")
                                                        name,z=y.split("; Age:")
                                                        n1,n2=name.split(" ")
                                                        n1=decode(n1)
                                                        n2=decode(n2)
                                                        name=n1+" "+n2
                                                        z2,aval_bal=z.split("; Balance: ")
                                                        actual_bal,typ=aval_bal.split(";")
                                                        actual_bal=decode(actual_bal)
                                                        
                                                tmsg.askokcancel("Status",f"Account Number: {a_num.get()};Name: {name}; Available Balance: {actual_bal} ")    
                                
                                        def ext():
                                            new_root2.destroy()
                                            new_root.destroy()
                                            root.deiconify()
                                        def deposit():
                                            new_root2.withdraw()
                                            root3=Toplevel(new_root2)
                                            root3.geometry("1280x800")
                                            root3.minsize(1280,800)
                                            root3.maxsize(1280,800)
                                            root3.wm_iconbitmap(r"assets\atmicon.ico")
                                            root3.title("ATM DEPOSIT")
                                            # root3.configure(bg="black")
                                            
                                            image=Image.open(r"assets\d.jpg")
                                            photo=ImageTk.PhotoImage(image)
                                            
                                            background_label =Label(root3, image=photo)
                                            background_label.place(x=0, y=0, relwidth=1, relheight=1)

                                            
                                            def update_clock():
                                                current_time = datetime.now().strftime("Date: %Y-%m-%d & Time: %H:%M:%S")
                                                label.config(text=current_time)
                                                label.after(1000, update_clock)
                                            
                                            def validate_input(new_value):
                                                return len(new_value) <= 11
                                            
                                            f=Frame(root3,bg="light blue",relief="solid",borderwidth=4)
                                            f.pack(expand=True)
                                            
                                            Label(f,text="Enter Your 11 Digit Account Number",font="arial 28 bold",bg="light blue",padx=20).pack(pady=30,fill=X)
                                            varr=StringVar()
                                            acn=Entry(f,textvariable=varr,font="arial 40 bold",relief="solid",width=20,bg="light blue",justify="center",borderwidth=4,validate="key", validatecommand=(root.register(validate_input), "%P"))
                                            acn.pack(pady=30)
                                            f2=Frame(f,bg="light blue")
                                            f2.pack()
                                            def sub():
                                                Ac2=acn.get().strip()
                                                with open("History.txt","r") as f:
                                                    data=f.readlines()
                                                    if len(data)>0:
                                                        if Ac2:
                                                            if Ac2.isdigit() and len(Ac2)==11:
                                                                if Ac==get_binary(acn.get()):
                                                                    with open("ATM.txt","r+") as f:
                                                                        data=f.readlines()
                                                                        for i in data:
                                                                            if i.startswith("Account Number: "+Ac):#Ac and acn.get() is same
                                                                                i = i[len("Account Number: "):]
                                                                                x,b=i.split("; Customer Name: ")
                                                                                x=decode(x)
                                                                                y,c=b.split("; Age:")
                                                                                n1,n2=y.split(" ")
                                                                                n1=decode(n1)
                                                                                n2=decode(n2)
                                                                                y=n1+" "+n2
                                                                                z,d=c.split("; Balance: ")
                                                                                w,e=d.split(";")
                                                                        val=tmsg.askokcancel("Status",f"Please Verify The Details\nAccount Number: {x} and Customer Name: {y}")
                                                                        if val==True:
                                                                            root3.destroy()
                                                                            root4=Toplevel(new_root2)
                                                                            root4.geometry("1280x800")
                                                                            root4.minsize(1280,800)
                                                                            root4.maxsize(1280,800)
                                                                            root4.wm_iconbitmap(r"assets\atmicon.ico")
                                                                            root4.title("ATM DEPOSIT")
                                                                            # root4.configure(bg="black")
                                                                            
                                                                            image=Image.open(r"assets\a.jpg")
                                                                            photo=ImageTk.PhotoImage(image)
                                                                            
                                                                            background_label =Label(root4, image=photo)
                                                                            background_label.place(x=0, y=0, relwidth=1, relheight=1)
                                                                            
                                                                            def update_clock():
                                                                                current_time = datetime.now().strftime("Date: %Y-%m-%d & Time: %H:%M:%S")
                                                                                label.config(text=current_time)
                                                                                label.after(1000, update_clock)
                                                                            f=Frame(root4,bg="light blue")
                                                                            f.pack(expand=True)
                                                                            
                                                                            Label(f,text="Enter Amount to Deposit",font="arial 28 bold",bg="light blue").pack(pady=10,fill=X)
                                                                            Label(f,text="Deposit Limit 50000/- Per Day",font="arial 28 bold",bg="red",pady=10).pack(fill=X)
                                                                            var1=StringVar()
                                                                            acn1=Entry(f,textvariable=var1,font="arial 40 bold",relief="solid",width=20,bg="light blue",justify="center",borderwidth=4)
                                                                            acn1.pack(pady=30,padx=30)
                                                                            f2=Frame(f,bg="light blue")
                                                                            f2.pack()
                                                                    
                                                                            def sub1():
                                                                                Ac1=acn1.get().strip()
                                                                                if Ac1:
                                                                                    if Ac1.isdigit() and int(Ac1)>0:
                                                                                        pygame.init()
                                                                                        audio_path = r"assets\machine sound.mp3"
                                                                                        pygame.mixer.music.load(audio_path)
                                                                                        pygame.mixer.music.play()
                                                                                        # tmsg.askokcancel("Status","Please Wait!...Counting Is Under Progress...")
                                                                                        pygame.time.delay(6000)
                                                                                        pygame.quit()
                                                                                        if int(Ac1)<=50000:
                                                                                            with open("Balance.txt","a") as file:
                                                                                                file.write(f"{acn1.get()}\n")
                                                                                            root4.withdraw()
                                                                                            root5=Toplevel(root4)
                                                                                            root5.geometry("1280x800")
                                                                                            root5.minsize(1280,800)
                                                                                            root5.maxsize(1280,800)
                                                                                            root5.wm_iconbitmap(r"assets\atmicon.ico")
                                                                                            root5.title("ATM DEPOSIT")
                                                                                            # root5.configure(bg="black")
                                                                                            image=Image.open(r"assets\b.jpg")
                                                                                            photo=ImageTk.PhotoImage(image)
                                                                                            
                                                                                            background_label =Label(root5, image=photo)
                                                                                            background_label.place(x=0, y=0, relwidth=1, relheight=1)
                                                                                            
                                                                                            def update_clock():
                                                                                                current_time = datetime.now().strftime("Date: %Y-%m-%d & Time: %H:%M:%S")
                                                                                                label.config(text=current_time)
                                                                                                label.after(1000, update_clock)
                                                                                            
                                                                                            fr4=Frame(root5,bg="lavender",relief="solid",borderwidth=5)
                                                                                            fr4.pack(expand=True)
                                                                                            
                                                                                            with open("Balance.txt","r") as file:
                                                                                                    data=file.readlines()
                                                                                                    l=[]
                                                                                                    for i in range(len(data)):
                                                                                                        ele=int(data[i])
                                                                                                        l.append(ele)
                                                                                                    bal_sum=sum(l)    
                                                                                            Label(fr4,text="Deposit Summery",font="arial 28 bold",bg="yellow",pady=10).pack(pady=10,fill=BOTH)
                                                                                            Label(fr4,text=f"Proceed to Deposit of Rs [{bal_sum}] to Your Saving Account?",font="arial 28 bold",bg="lavender").pack(pady=30,fill=X,padx=15)
                                                                                            f3=Frame(fr4,bg="aqua",relief=SOLID,borderwidth=4)
                                                                                            f3.pack(pady=20)
                                                                                            def ext3():
                                                                                                with open("Balance.txt","r") as file:
                                                                                                    data=file.readlines()
                                                                                                    l=[]
                                                                                                    for i in range(len(data)):
                                                                                                        ele=int(data[i])
                                                                                                        l.append(ele)
                                                                                                    bal_sum=sum(l)
                                                                                                    val3=tmsg.askokcancel("Status",f"Session Cancelled...\nPlease Kindly Collect Your Depositted Cash of Rs [{bal_sum}]")
                                                                                                    if val3==True:
                                                                                                        with open("Balance.txt","w") as file:
                                                                                                            pass
                                                                                                        root5.destroy()
                                                                                                        new_root2.deiconify()
                                                                                            def proceed():
                                                                                                today = datetime.today().strftime("%Y-%m-%d")
                                                                                                
                                                                                                with open("History.txt","a") as f:
                                                                                                    f.write(f"CDEPOSIT|{Ac}|{today}|{bal_sum}\n")
                                                                                                with open("History.txt","r") as f:
                                                                                                    history=f.readlines()
                                                                                                    element=[]
                                                                                                    for i in history:
                                                                                                        if i.startswith("CDEPOSIT|"+Ac):
                                                                                                            w,x,y,z=i.split("|")
                                                                                                            z=int(z)
                                                                                                            if y==today:
                                                                                                                element.append(z)
                                                                                                    a=sum(element)
                                                                                                    if a>50000:
                                                                                                        val3=tmsg.askyesnocancel("Status",f"Your Maximum Deposit Limit Exceed for Today!\nYou Can Add Cash/Make Deposit Tomorrow Again...\n**Please Collect The Cash Rs {bal_sum}**\n\nPress: Yes -to Know about Your Deposit Limit for Today")
                                                                                                        with open("History.txt","r+") as f:
                                                                                                            history=f.readlines()
                                                                                                            f.seek(0)
                                                                                                            f.truncate()
                                                                                                            f.writelines(history[:-1])
                                                                                                        with open("Balance.txt","w") as f:
                                                                                                            pass    
                                                                                                        if val3==True:
                                                                                                            with open("History.txt","r") as f:
                                                                                                                data=f.readlines()
                                                                                                                element=[]
                                                                                                                for i in data:
                                                                                                                    if i.startswith("CDEPOSIT|"+Ac):
                                                                                                                        w,x,y,z=i.split("|")
                                                                                                                        z=int(z)
                                                                                                                        if y==today:
                                                                                                                            element.append(z)
                                                                                                                a=sum(element)
                                                                                                                b=50000-a
                                                                                                            val4=tmsg.askokcancel("Know Your Deposit Limit",f"You can Deposit upto Rs {b} Today")
                                                                                                            if val4==True and (b>0 and b<50000):
                                                                                                                root5.destroy()
                                                                                                                root4.deiconify()
                                                                                                            else:
                                                                                                                root5.destroy()
                                                                                                                new_root2.deiconify()
                                                                                                        elif val3==False:
                                                                                                            root5.destroy()
                                                                                                            new_root2.deiconify()
                                                                                                        else:
                                                                                                            root5.destroy()
                                                                                                            new_root2.deiconify()
                                                                                                    else:
                                                                                                        with open("ATM.txt","r+") as file:
                                                                                                            data=file.readlines()
                                                                                                            file.seek(0)#It moves the cursor to the starting Position of the txt file
                                                                                                            for i in data:
                                                                                                                if i.startswith("Account Number: "+Ac):
                                                                                                                    details,balance=i.split("; Balance: ")
                                                                                                                    balance,extra=balance.split(";")
                                                                                                                    balance=decode(balance)
                                                                                                                    int_balance=int(balance)
                                                                                                                    int_balance=int_balance+int(bal_sum)
                                                                                                                    balance=str(int_balance)
                                                                                                                    balance=get_binary(balance)
                                                                                                                    i=details+"; Balance: "+balance+";"+extra
                                                                                                                file.write(i)
                                                                                                            with open("Balance.txt","w") as f:
                                                                                                                pass
                                                                                                            val2=tmsg.askokcancel("Status",f"Deposit of Rs {bal_sum} Successful...")
                                                                                                            if val2==False:
                                                                                                                root5.destroy()
                                                                                                                new_root2.deiconify()
                                                                                                            else:
                                                                                                                root5.destroy()
                                                                                                                new_root2.deiconify()
                                                                                                        with open("History.txt","r+") as f:
                                                                                                            data=f.readlines()
                                                                                                            f.seek(0)
                                                                                                            for i in data:
                                                                                                                if i.startswith("ABALANCE|"):
                                                                                                                    a,b,c,d=i.split("|")
                                                                                                                    d=int(d)
                                                                                                                    d=d+int(bal_sum)
                                                                                                                    d=str(d)
                                                                                                                    i=a+"|"+b+"|"+c+"|"+d+"\n"
                                                                                                                f.write(i)
                                                                                            def add_more():
                                                                                                val2=tmsg.askokcancel("Status","Do You Want to Add More Cash?")  
                                                                                                if val2==True:
                                                                                                    root5.withdraw()
                                                                                                    root4.deiconify()
                                                                                            Button(f3,text="Cancel",font="arial 20 bold",relief="raised",bg="Red",padx=10,command=ext3).grid(row=0,column=0,pady=10,padx=75)
                                                                                            Button(f3,text="Add More Cash",font="arial 20 bold",relief="raised",bg="blue",fg="white",command=add_more).grid(row=0,column=1,pady=10,padx=75)
                                                                                            Button(f3,text="Proceed",font="arial 20 bold",relief="raised",bg="light green",padx=5,command=proceed).grid(row=0,column=2,pady=10,padx=75)
                                                                                            
                                                                                            f4=Frame(fr4,bg="yellow")
                                                                                            f4.pack(fill=X)
                                                                                            label=Label(f4,fg="blue",bg="yellow",font="arial 20 bold")
                                                                                            label.pack(fill=X)
                                                                                            update_clock()
                                                                                            root5.mainloop()
                                                                                        else:
                                                                                            v1=tmsg.askokcancel("Status","You Can not Deposit More than Rs 50000")
                                                                                            if v1==True:
                                                                                                var1.set("")
                                                                                            else:
                                                                                                root4.destroy()
                                                                                                new_root2.deiconify()
                                                                                    else:
                                                                                        v2=tmsg.askokcancel("Status", "Please Enter a Valid Amount")
                                                                                        if v2==True:
                                                                                            var1.set("")
                                                                                        else:
                                                                                            root4.destroy()
                                                                                            new_root2.deiconify()
                                                                                else:
                                                                                    tmsg.askokcancel("Status", "Please Enter The Amount")        
                                                                            def ext2():
                                                                                with open("Balance.txt","r") as f:
                                                                                    data=f.readlines()
                                                                                    if len(data)==0:
                                                                                        root4.destroy()
                                                                                        new_root2.deiconify()
                                                                                    else:
                                                                                        l=[]
                                                                                        for i in range(len(data)):
                                                                                            ele=int(data[i])
                                                                                            l.append(ele)
                                                                                        bal_sum=sum(l)
                                                                                        val4=tmsg.askokcancel("Status",f"Session Cancelled...\nPlease Kindly Collect Your Depositted Cash of Rs [{bal_sum}]")
                                                                                        if val4== True:
                                                                                            with open("Balance.txt","w") as file:
                                                                                                pass
                                                                                            root4.destroy()
                                                                                            new_root2.deiconify()
                                                                            Button(f2,text="Cancel",font="arial 20 bold",relief="raised",bg="Red",padx=5,command=ext2).grid(row=0,column=0,pady=30)
                                                                            Label(f2,text="",font="arial 20 bold",bg="light blue").grid(row=0,column=1,padx=90)
                                                                            Button(f2,text="Submit",bg="light green",font="arial 20 bold",relief="raised",command=sub1).grid(row=0,column=2,pady=30)
                                                                            f3=Frame(f,bg="yellow")
                                                                            f3.pack(fill=X)
                                                                            label=Label(f3,fg="blue",bg="yellow",font="arial 20 bold")
                                                                            label.pack(fill=X)
                                                                            update_clock()
                                                                            root4.mainloop()
                                                                        else:
                                                                            pass
                                                                else:
                                                                    val=tmsg.askokcancel("Status","Account Number Mismatch!....Please Re-enter Account Number...") 
                                                                    if val==True:
                                                                        varr.set("")
                                                            else:
                                                                val1=tmsg.askokcancel("Status","Please Enter a Valid Account Number....")
                                                                if val1==True:
                                                                    varr.set("")
                                                        else:
                                                            tmsg.askokcancel("Status","Please Enter The Account Number....") 
                                                    else:
                                                        tmsg.askokcancel("Status","SORRY!...This Service Is Not Available Right Now....") 
                                                        root3.destroy()
                                                        new_root2.deiconify()
                                            def ext1():
                                                root3.destroy()
                                                new_root2.deiconify()
                                            Button(f2,text="Cancel",font="arial 20 bold",relief="raised",bg="Red",command=ext1,padx=5).grid(row=0,column=0,pady=30)
                                            Label(f2,text="",font="arial 20 bold",bg="light blue").grid(row=0,column=1,padx=90)
                                            Button(f2,text="Submit",bg="light green",font="arial 20 bold",relief="raised",command=sub).grid(row=0,column=2,pady=30)
                                            f3=Frame(f,bg="yellow")
                                            f3.pack(fill=X)
                                            label=Label(f3,fg="blue",bg="yellow",font="arial 20 bold")
                                            label.pack(fill=X)
                                            update_clock()
                                            root3.mainloop()
                                        def withdraw():
                                            new_root2.withdraw()
                                            root3=Toplevel(new_root2)
                                            root3.geometry("1280x800")
                                            root3.minsize(1280,800)
                                            root3.maxsize(1280,800)
                                            root3.wm_iconbitmap(r"assets\atmicon.ico")
                                            root3.title("ATM WITHDRAW")
                                            # root3.configure(bg="black")
                                            
                                            image=Image.open(r"assets\a.jpg")
                                            photo=ImageTk.PhotoImage(image)
                                                                    
                                            background_label =Label(root3, image=photo)
                                            background_label.place(x=0, y=0, relwidth=1, relheight=1)
                                            
                                            def update_clock():
                                                current_time = datetime.now().strftime("Date: %Y-%m-%d & Time: %H:%M:%S")
                                                label.config(text=current_time)
                                                label.after(1000, update_clock)
                                                
                                            f=Frame(root3,bg="light blue",relief="solid",borderwidth=5)
                                            f.pack(expand=True)
                                            
                                            Label(f,text="Enter Withdraw Amount",font="arial 28 bold",bg="light blue").pack(pady=10,fill=X)
                                            Label(f,text="Withdraw Limit 50000/- Per Day",font="arial 28 bold",bg="red",pady=10).pack(fill=X)
                                            varr=StringVar()
                                            w_amount=Entry(f,textvariable=varr,font="arial 40 bold",relief="solid",width=20,bg="light blue",justify="center",borderwidth=4)
                                            w_amount.pack(pady=30,padx=30)
                                            
                                            f2=Frame(f,bg="light blue")
                                            f2.pack()
                                            
                                            def ext1():
                                                root3.destroy()
                                                new_root2.deiconify()
                                            
                                            def sub():
                                                with open("History.txt","r") as f:
                                                    data=f.readlines()
                                                    if len(data)>0:
                                                        if w_amount.get(): 
                                                            if w_amount.get().isdigit() and int(w_amount.get())>0:
                                                                if int(w_amount.get())<=50000:
                                                                    root3.withdraw()
                                                                    root4=Toplevel(root3)
                                                                    root4.geometry("1280x800")
                                                                    root4.minsize(1280,800)
                                                                    root4.maxsize(1280,800)
                                                                    root4.wm_iconbitmap(r"assets\atmicon.ico")
                                                                    root4.title("ATM WITHDRAW")
                                                                    # root4.configure(bg="black")
                                                                    
                                                                    image=Image.open(r"assets\d.jpg")
                                                                    photo=ImageTk.PhotoImage(image)
                                                                            
                                                                    background_label =Label(root4, image=photo)
                                                                    background_label.place(x=0, y=0, relwidth=1, relheight=1)
                                                                    
                                                                    def update_clock():
                                                                        current_time = datetime.now().strftime("Date: %Y-%m-%d & Time: %H:%M:%S")
                                                                        label.config(text=current_time)
                                                                        label.after(1000, update_clock)
                                                                        
                                                                    def validate_input(new_value):
                                                                        return len(new_value) <= 4
                                                                    
                                                                    f=Frame(root4,bg="light blue",relief="solid",borderwidth=5)
                                                                    f.pack(expand=True)
                                                                                            
                                                                    Label(f,text="Enter Your PIN/Secret Number",font="arial 28 bold",bg="light blue").pack(pady=10,fill=X)
                                                                    Label(f,text="CAUTION",font="arial 28 bold",bg="yellow").pack(pady=10)
                                                                    Label(f,text="Please Hide Your PIN And Don't Tell Your PIN to Anyone!",font="arial 28 bold",bg="red",pady=10,padx=10).pack(fill=X)
                                                                    var1=StringVar()
                                                                    pin=Entry(f,textvariable=var1,font="arial 40 bold",relief="solid",width=20,bg="light blue",justify="center",borderwidth=4, validate="key", validatecommand=(root.register(validate_input), "%P"),show="*")
                                                                    pin.pack(pady=30,padx=30)
                                                                    f2=Frame(f,bg="light blue")
                                                                    f2.pack()
                                                                    
                                                                    def ext2():
                                                                        root4.destroy()
                                                                        new_root2.deiconify()
                                                                        
                                                                    def sub1():
                                                                        def get_binary(x):
                                                                            binary_value="".join(format(ord(i),"08b") for i in x)
                                                                            return binary_value

                                                                        def decode(x):
                                                                            original_data=" ".join(x[i:i+8] for i in range(0,len(x),8))
                                                                            data=original_data.split()
                                                                            decimal_value= ''.join(chr(int(i, 2)) for i in data)
                                                                            return decimal_value
                                                                        today = datetime.today().strftime("%Y-%m-%d")
                                                                        if pin.get(): 
                                                                            if pin.get().isdigit() and len(pin.get())==4:                                 
                                                                                with open("History.txt","a") as f:
                                                                                    f.write(f"WITHDRAW|{Ac}|{today}|{w_amount.get()}\n")
                                                                                with open("History.txt","r") as f:
                                                                                    history=f.readlines()
                                                                                    element=[]
                                                                                    for i in history:
                                                                                        if i.startswith("WITHDRAW|"+Ac):
                                                                                            w,x,y,z=i.split("|")
                                                                                            z=int(z)
                                                                                            if y==today:
                                                                                                element.append(z)
                                                                                    a=sum(element)
                                                                                    if a>50000:
                                                                                        val3=tmsg.askyesnocancel("Status",f"Your Maximum Withdraw Limit Exceed for Today!\nYou Can Cash Withdraw Tomorrow Again...\n\nPress: Yes -to Know about Your Withdrawl Limit for Today")
                                                                                        with open("History.txt","r+") as f:
                                                                                            history=f.readlines()
                                                                                            f.seek(0)
                                                                                            f.truncate()
                                                                                            f.writelines(history[:-1])
                                                                                        if val3==True:
                                                                                            with open("History.txt","r") as f:
                                                                                                data=f.readlines()
                                                                                                element=[]
                                                                                                for i in data:
                                                                                                    if i.startswith("WITHDRAW|"+Ac):
                                                                                                        w,x,y,z=i.split("|")
                                                                                                        z=int(z)
                                                                                                        if y==today:
                                                                                                            element.append(z)
                                                                                                a=sum(element)
                                                                                                b=50000-a
                                                                                            val4=tmsg.askokcancel("Know Your Withdrawl Limit",f"You can Withdrawl upto Rs {b} Today")
                                                                                            if val4==True and (b>0 and b<50000):
                                                                                                root4.destroy()
                                                                                                root3.deiconify()
                                                                                            else:
                                                                                                root4.destroy()
                                                                                                new_root2.deiconify()
                                                                                        elif val3==False:
                                                                                            root4.destroy()
                                                                                            new_root2.deiconify()
                                                                                        else:
                                                                                            root4.destroy()
                                                                                            new_root2.deiconify()
                                                                                    else:
                                                                                        with open("ATM.txt","r+") as file:
                                                                                            data=file.readlines()
                                                                                            file.seek(0)#It moves the cursor to the starting Position of the txt file
                                                                                            for i in data:
                                                                                                if i.startswith("Account Number: "+Ac):
                                                                                                    details,x=i.split("; PIN: ")
                                                                                                    PIN,y=x.split("; Balance: ")
                                                                                                    PIN=decode(PIN)
                                                                                                    balance,extra=y.split(";")
                                                                                                    balance=decode(balance)
                                                                                                    int_balance=int(balance)
                                                                                                    if PIN!=pin.get():
                                                                                                        v2=tmsg.askokcancel("Status","SORRY!...Wrong Pin!")
                                                                                                        with open("History.txt","r+") as f:
                                                                                                            history=f.readlines()
                                                                                                            f.seek(0)
                                                                                                            f.truncate()
                                                                                                            f.writelines(history[:-1])
                                                                                                        if v2==True:
                                                                                                            root4.destroy()
                                                                                                            new_root2.deiconify()
                                                                                                        else:
                                                                                                            root4.destroy()
                                                                                                            new_root2.deiconify()
                                                                                                    elif int(w_amount.get())>int_balance:
                                                                                                        v3=tmsg.askokcancel("Status","SORRY!...You Don't Have Sufficient Balance in Your Accout...")
                                                                                                        with open("History.txt","r+") as f:
                                                                                                            history=f.readlines()
                                                                                                            f.seek(0)
                                                                                                            f.truncate()
                                                                                                            f.writelines(history[:-1])
                                                                                                        if v3==True:
                                                                                                            root4.destroy()
                                                                                                            new_root2.deiconify()
                                                                                                        else:
                                                                                                            root4.destroy()
                                                                                                            new_root2.deiconify()
                                                                                                    else:
                                                                                                        with open("History.txt","r") as f:
                                                                                                            data1=f.readlines()
                                                                                                            # f.seek(0)
                                                                                                            for index,j in enumerate(data1):
                                                                                                                if j.startswith("ABALANCE|"):
                                                                                                                    a,b,c,d=j.split("|")
                                                                                                                    d=int(d)
                                                                                                                    if int(w_amount.get())>d:
                                                                                                                        with open("History.txt","r+") as f:
                                                                                                                            history=f.readlines()
                                                                                                                            f.seek(0)
                                                                                                                            f.truncate()
                                                                                                                            f.writelines(history[:-1])
                                                                                                                        tmsg.askokcancel("Status","ATM Can not Disburse Any Amount Right Now....Please Try After Some Time")
                                                                                                                        root4.destroy()
                                                                                                                        new_root2.deiconify()
                                                                                                                    else:
                                                                                                                        int(w_amount.get())<=int_balance and PIN==pin.get()
                                                                                                                        int_balance=int_balance-int(w_amount.get())
                                                                                                                        balance=str(int_balance)
                                                                                                                        balance=get_binary(balance)
                                                                                                                        PIN=get_binary(PIN)
                                                                                                                        i=details+"; PIN: "+PIN+"; Balance: "+balance+";"+extra
                                                                                                                        pygame.init()
                                                                                                                        audio_path = r"assets\machine sound.mp3"
                                                                                                                        pygame.mixer.music.load(audio_path)
                                                                                                                        pygame.mixer.music.play()
                                                                                                                        # tmsg.askokcancel("Status","Please Wait!...Counting Is Under Progress...")
                                                                                                                        pygame.time.delay(6000)
                                                                                                                        pygame.quit()
                                                                                                                        val2=tmsg.askokcancel("Status",f"Withdrawl of Rs {w_amount.get()} Successful...")
                                                                                                                        if val2==False:
                                                                                                                            root4.destroy()
                                                                                                                            new_root2.deiconify()
                                                                                                                        else:
                                                                                                                            root4.destroy()
                                                                                                                            new_root2.deiconify()
                                                                                                                        d=d-int(w_amount.get())
                                                                                                                        d=str(d)
                                                                                                                        data1[index]=a+"|"+b+"|"+c+"|"+d+"\n"
                                                                                                    
                                                                                                                        with open("History.txt","w") as f:
                                                                                                                                f.writelines(data1) 
                                                                                                file.write(i)
                                                                                            file.truncate()       
                                                                            else:
                                                                                v4=tmsg.askokcancel("Status","Please Enter A Valid PIN.....")
                                                                                if v4==True:
                                                                                    var1.set("")  
                                                                                else:
                                                                                    root3.destroy()
                                                                                    new_root2.deiconify()
                                                                        else:
                                                                            tmsg.askokcancel("Status","Please Enter PIN/Secret Number....")
                                                                    Button(f2,text="Cancel",font="arial 20 bold",relief="raised",bg="Red",padx=5,command=ext2).grid(row=0,column=0,pady=30)
                                                                    Label(f2,text="",font="arial 20 bold",bg="light blue").grid(row=0,column=1,padx=90)
                                                                    Button(f2,text="Submit",bg="light green",font="arial 20 bold",relief="raised",command=sub1).grid(row=0,column=2,pady=30)
                                                                    
                                                                    f3=Frame(f,bg="yellow")
                                                                    f3.pack(fill=X)
                                                                    label=Label(f3,fg="blue",bg="yellow",font="arial 20 bold")
                                                                    label.pack(fill=X)
                                                                    update_clock()
                                                                    root4.mainloop() 
                                                                else:
                                                                    v=tmsg.askokcancel("Status","You Can not Withdraw More than Rs 50000")
                                                                    if v==True:
                                                                        varr.set("")  
                                                                    else:
                                                                        root3.destroy()
                                                                        new_root2.deiconify() 
                                                            else:
                                                                v1=tmsg.askokcancel("Status","Please Enter A Valid Amount....")  
                                                                if v1==True:
                                                                    varr.set("")  
                                                                else:
                                                                    root3.destroy()
                                                                    new_root2.deiconify()                                                                                                             
                                                        else:
                                                            tmsg.askokcancel("Status","Please Enter The Amount....")
                                                    else:
                                                        tmsg.askokcancel("Status","SORRY!...This Service Is Not Available Right Now....")
                                                        root3.destroy()
                                                        new_root2.deiconify()
                                            Button(f2,text="Cancel",font="arial 20 bold",relief="raised",bg="Red",padx=5,command=ext1).grid(row=0,column=0,pady=30)
                                            Label(f2,text="",font="arial 20 bold",bg="light blue").grid(row=0,column=1,padx=90)
                                            Button(f2,text="Submit",bg="light green",font="arial 20 bold",relief="raised",command=sub).grid(row=0,column=2,pady=30)
                                            f3=Frame(f,bg="yellow")
                                            f3.pack(fill=X)
                                            label=Label(f3,fg="blue",bg="yellow",font="arial 20 bold")
                                            label.pack(fill=X)
                                            update_clock()
                                            root3.mainloop()
                                        def pin_change():
                                            new_root2.withdraw()
                                            root3=Toplevel(new_root2)
                                            root3.geometry("1280x800")
                                            root3.minsize(1280,800)
                                            root3.maxsize(1280,800)
                                            root3.wm_iconbitmap(r"assets\atmicon.ico")
                                            root3.title("ATM PIN CHANGE")
                                            # root3.configure(bg="black")
                                            image=Image.open(r"assets\a.jpg")
                                            photo=ImageTk.PhotoImage(image)
                                                                    
                                            background_label =Label(root3, image=photo)
                                            background_label.place(x=0, y=0, relwidth=1, relheight=1)
                                            
                                            def update_clock():
                                                current_time = datetime.now().strftime("Date: %Y-%m-%d & Time: %H:%M:%S")
                                                label.config(text=current_time)
                                                label.after(1000, update_clock)
                                            def validate_input(new_value):
                                                return len(new_value) <= 11
                                            
                                            f=Frame(root3,bg="light blue")
                                            f.pack(expand=True)
                                            
                                            Label(f,text="Enter Your 11 Digit Account Number",font="arial 28 bold",bg="light blue",padx=20).pack(pady=30,fill=X)
                                            varr=StringVar()
                                            acn=Entry(f,textvariable=varr,font="arial 40 bold",relief="solid",width=20,bg="light blue",justify="center",borderwidth=4,validate="key", validatecommand=(root.register(validate_input), "%P"))
                                            acn.pack(pady=30)
                                            f2=Frame(f,bg="light blue")
                                            f2.pack()
                                            def ext1():
                                                root3.destroy()
                                                new_root2.deiconify()
                                            def sub():
                                                if acn.get():
                                                    if acn.get().isdigit() and len(acn.get())==11:
                                                        if acn.get()==a_num.get():
                                                            root3.withdraw()
                                                            root4=Toplevel(root3)
                                                            root4.geometry("1280x800")
                                                            root4.minsize(1280,800)
                                                            root4.maxsize(1280,800)
                                                            root4.wm_iconbitmap(r"assets\atmicon.ico")
                                                            root4.title("ATM PIN CHANGE")
                                                            # root4.configure(bg="black")
                                                            
                                                            image=Image.open(r"assets\d.jpg")
                                                            photo=ImageTk.PhotoImage(image)
                                                                    
                                                            background_label =Label(root4, image=photo)
                                                            background_label.place(x=0, y=0, relwidth=1, relheight=1)
                                                            
                                                            def update_clock():
                                                                current_time = datetime.now().strftime("Date: %Y-%m-%d & Time: %H:%M:%S")
                                                                label.config(text=current_time)
                                                                label.after(1000, update_clock)
                                                                
                                                            def validate_input(new_value):
                                                                return len(new_value) <= 4
                                                            
                                                            f=Frame(root4,bg="light blue",relief="solid",borderwidth=5)
                                                            f.pack(expand=True)
                                                                                    
                                                            Label(f,text="Enter Your (OLD) PIN/Secret Number",font="arial 28 bold",bg="orange").pack(pady=10,fill=X)
                                                            Label(f,text="CAUTION",font="arial 28 bold",bg="yellow").pack(pady=10)
                                                            Label(f,text="Please Hide Your PIN And Don't Tell Your PIN to Anyone!",font="arial 28 bold",bg="red",pady=10,padx=10).pack(fill=X)
                                                            varr1=StringVar()
                                                            pin=Entry(f,textvariable=varr1,font="arial 40 bold",relief="solid",width=20,bg="light blue",justify="center",borderwidth=4, validate="key", validatecommand=(root.register(validate_input), "%P"),show="*")
                                                            pin.pack(pady=30,padx=30)
                                                            f2=Frame(f,bg="light blue")
                                                            f2.pack()
                                                            
                                                            def ext2():
                                                                root4.destroy()
                                                                new_root2.deiconify()
                                                            
                                                            def sub1():
                                                                def get_binary(x):
                                                                    binary_value="".join(format(ord(i),"08b") for i in x)
                                                                    return binary_value

                                                                def decode(x):
                                                                    original_data=" ".join(x[i:i+8] for i in range(0,len(x),8))
                                                                    data=original_data.split()
                                                                    decimal_value= ''.join(chr(int(i, 2)) for i in data)
                                                                    return decimal_value
                                                                with open("ATM.txt","r") as f:
                                                                    data=f.readlines()
                                                                    for i in data:
                                                                        if i.startswith("Account Number: "+Ac):
                                                                            x,y=i.split("; PIN: ")
                                                                            PIN,extra=y.split("; Balance: ")
                                                                            PIN=decode(PIN)
                                                                            if pin.get():
                                                                                if pin.get().isdigit() and len(pin.get())==4:
                                                                                    if pin.get()==PIN:      
                                                                                        root4.withdraw()
                                                                                        root5=Toplevel(root3)
                                                                                        root5.geometry("1280x800")
                                                                                        root5.minsize(1280,800)
                                                                                        root5.maxsize(1280,800)
                                                                                        root5.configure(bg="aqua")
                                                                                        root5.wm_iconbitmap(r"assets\atmicon.ico")
                                                                                        root5.title("ATM PIN CHANGE")
                                                                                        
                                                                                        def update_clock():
                                                                                            current_time = datetime.now().strftime("Date: %Y-%m-%d & Time: %H:%M:%S")
                                                                                            label.config(text=current_time)
                                                                                            label.after(1000, update_clock)
                                                                                            
                                                                                        def validate_input(new_value):
                                                                                            return len(new_value) <= 4
                                                                                        
                                                                                        Label(root5,text="Change Your 4 digit Pin/Secret Number",font="arial 28 bold",bg="yellow").pack(fill=X)
                                                                                        Label(root5,text="",font="arial 20 bold",bg="aqua").pack(fill=X)
                                                                                        
                                                                                        of=Frame(root5,bg="black",relief="solid",borderwidth=4)
                                                                                        of.pack()
                                                                                                                
                                                                                        Label(of,text="Create Your PIN/Secret Number",font="arial 28 bold",bg="orange").pack(pady=10,fill=X)
                                                                                        Label(of,text="CAUTION",font="arial 28 bold",bg="yellow").pack(pady=10)
                                                                                        Label(of,text="Please Hide Your PIN And Don't Tell Your PIN to Anyone!",font="arial 28 bold",bg="red",pady=10,padx=10).pack(fill=X)
                                                                                        
                                                                                        f=Frame(of,bg="yellow",relief="solid",borderwidth=4)
                                                                                        f.pack(pady=15)
                                                                                    
                                                                                        var1=StringVar()
                                                                                        Label(f,text=f"Create New-PIN:",font="arial 20 bold",bg="yellow",fg="black").grid(row=0,column=0,padx=20,pady=20)
                                                                                        p1=Entry(f,textvariable=var1,font="arial 30 bold",relief="sunken",width=20,justify="center",validate="key", validatecommand=(root.register(validate_input), "%P"))
                                                                                        p1.grid(row=0,column=1,padx=20,pady=20)
                                                                                        def a1():
                                                                                            if p1.get():
                                                                                                if p1.get().isdigit() and len(p1.get())==4:
                                                                                                    tmsg.askokcancel("Status","Successfully Added New-PIN...")
                                                                                                else:
                                                                                                   v3=tmsg.askokcancel("Status","Please Enter Valid 4 Digit PIN Without Any Characters...")
                                                                                                   if v3==True:
                                                                                                       var1.set("")
                                                                                            else:
                                                                                                v6=tmsg.askokcancel("Status","Please Enter New-PIN...")
                                                                                                if v6==True:
                                                                                                    var1.set("")
                                                                                        ad1=Button(f,text="Add",bg="green",font="arial 16 bold",fg="White",relief="raised",command=a1)
                                                                                        ad1.grid(row=0,column=2,padx=20,pady=20)
                                                                                        
                                                                                        var2=StringVar()
                                                                                        Label(f,text=f"Re-Enter New-PIN:",font="arial 20 bold",bg="yellow",fg="black").grid(row=1,column=0,padx=20,pady=20)
                                                                                        p2=Entry(f,textvariable=var2,font="arial 30 bold",relief="sunken",width=20,justify="center",validate="key", validatecommand=(root.register(validate_input), "%P"))
                                                                                        p2.grid(row=1,column=1,padx=20,pady=20)
                                                                                        def a2():
                                                                                            if p2.get():
                                                                                                if p2.get().isdigit() and len(p2.get())==4:
                                                                                                    tmsg.askokcancel("Status","Successfully Added New-PIN...")
                                                                                                else:
                                                                                                   v7=tmsg.askokcancel("Status","Please Enter Valid 4 Digit PIN Without Any Characters...")
                                                                                                   if v7==True:
                                                                                                       var2.set("")
                                                                                            else:
                                                                                                v8=tmsg.askokcancel("Status","Please Re-Enter New-PIN...")
                                                                                                if v8==True:
                                                                                                    var2.set("")
                                                                                        ad2=Button(f,text="Add",bg="green",font="arial 16 bold",fg="White",relief="raised",command=a2)
                                                                                        ad2.grid(row=1,column=2,padx=20,pady=20)
                                                                                        
                                                                                        def ext3():
                                                                                            root5.destroy()
                                                                                            new_root2.deiconify()
                                                                                        
                                                                                        def sub2():
                                                                                            if p1.get() and p2.get():
                                                                                                if (len(p1.get())==4 and len(p2.get())==4) and (p1.get().isdigit()==True and p2.get().isdigit()==True):
                                                                                                    if p1.get() == p2.get():
                                                                                                        p=get_binary(p1.get())
                                                                                                        with open("ATM.txt","r+") as f:
                                                                                                            data=f.readlines()
                                                                                                            f.seek(0)
                                                                                                            for i in data:
                                                                                                                if i.startswith("Account Number: "+Ac):
                                                                                                                    x,y=i.split("; PIN: ")
                                                                                                                    PIN,extra=y.split("; Balance: ")
                                                                                                                    i=x+"; PIN: "+p+"; Balance: "+extra
                                                                                                                f.write(i)                        
                                                                                                        v3=tmsg.askokcancel("Status","PIN Changed Successfully....")
                                                                                                        if v3==True:
                                                                                                            root5.destroy()
                                                                                                            new_root2.deiconify()
                                                                                                        else:
                                                                                                            root5.destroy()
                                                                                                            new_root2.deiconify()
                                                                                                    else:
                                                                                                        tmsg.askokcancel("Status","Re-entered PIN is Different from New PIN!...")
                                                                                                        var2.set("")
                                                                                                        
                                                                                        f5=Frame(of,bg="black")
                                                                                        f5.pack()
                                                                                        
                                                                                        Button(f5,text="Cancel",font="arial 20 bold",relief="raised",bg="Red",padx=5,command=ext3).grid(row=2,column=0,pady=20)
                                                                                        Label(f5,text="",font="arial 20 bold",bg="black").grid(row=2,column=1,padx=90)
                                                                                        Button(f5,text="Submit",bg="light green",font="arial 20 bold",relief="raised",command=sub2).grid(row=2,column=2,pady=20)
                                                                                        
                                                                                        Label(root5,text="",font="arial 20 bold",bg="aqua").pack(pady=18)                                                           
                                                                                        
                                                                                        f3=Frame(root5,bg="yellow")
                                                                                        f3.pack(fill=X)
                                                                                        label=Label(f3,fg="blue",bg="yellow",font="arial 20 bold")
                                                                                        label.pack(fill=X)
                                                                                        update_clock()
                                                                                        root5.mainloop()
                                                                                    else:
                                                                                        v4=tmsg.askokcancel("Status","Old PIN Mismatch!...Please Enter Your Old PIN Correctly...")
                                                                                        if v4==True:
                                                                                            varr1.set("")
                                                                                else:
                                                                                    v5=tmsg.askokcancel("Status","Please Enter A Valid Old PIN...")
                                                                                    if v5==True:
                                                                                        varr1.set("")
                                                                            else:
                                                                                tmsg.askokcancel("Status","Please Enter Your Old PIN...")

                                                            Button(f2,text="Cancel",font="arial 20 bold",relief="raised",bg="Red",padx=5,command=ext2).grid(row=0,column=0,pady=30)
                                                            Label(f2,text="",font="arial 20 bold",bg="light blue").grid(row=0,column=1,padx=90)
                                                            Button(f2,text="Submit",bg="light green",font="arial 20 bold",relief="raised",command=sub1).grid(row=0,column=2,pady=30)
                                                            
                                                            f3=Frame(f,bg="yellow")
                                                            f3.pack(fill=X)
                                                            label=Label(f3,fg="blue",bg="yellow",font="arial 20 bold")
                                                            label.pack(fill=X)
                                                            update_clock()
                                                            root4.mainloop()
                                                        else:
                                                            v1=tmsg.askokcancel("Status","Account Number Mismatch!....Please Re-enter Account Number...") 
                                                            if v1==True:
                                                                varr.set("")
                                                    else:
                                                        v2=tmsg.askokcancel("Status","Please Enter A Valid Account Number....")
                                                        if v2==True:
                                                            varr.set("") 
                                                else:
                                                    tmsg.askokcancel("Status","Please Enter Account Number....")
                                            
                                            Button(f2,text="Cancel",font="arial 20 bold",relief="raised",bg="Red",command=ext1,padx=5).grid(row=0,column=0,pady=30)
                                            Label(f2,text="",font="arial 20 bold",bg="light blue").grid(row=0,column=1,padx=90)
                                            Button(f2,text="Submit",bg="light green",font="arial 20 bold",relief="raised",command=sub).grid(row=0,column=2,pady=30)
                                            f3=Frame(f,bg="yellow")
                                            f3.pack(fill=X)
                                            label=Label(f3,fg="blue",bg="yellow",font="arial 20 bold")
                                            label.pack(fill=X)
                                            update_clock()
                                            root3.mainloop()
                                        def forget_pin():
                                            new_root2.withdraw()
                                            root3=Toplevel(new_root2)
                                            root3.geometry("1280x800")
                                            root3.minsize(1280,800)
                                            root3.maxsize(1280,800)
                                            root3.wm_iconbitmap(r"assets\atmicon.ico")
                                            root3.title("ATM FORGET PIN")
                                            # root3.configure(bg="brown")
                                            
                                            image=Image.open(r"assets\d.jpg")
                                            photo=ImageTk.PhotoImage(image)
                                                                    
                                            background_label =Label(root3, image=photo)
                                            background_label.place(x=0, y=0, relwidth=1, relheight=1)
                                            
                                            def update_clock():
                                                current_time = datetime.now().strftime("Date: %Y-%m-%d & Time: %H:%M:%S")
                                                label.config(text=current_time)
                                                label.after(1000, update_clock)
                                            
                                            def get_captcha():
                                                str=string.ascii_letters+string.digits
                                                captcha="".join(random.choice(str) for i in range(6))
                                                return captcha
                                            
                                            def refresh_captcha():
                                                capt = get_captcha()
                                                captcha.config(text=capt)

                                            
                                            def validate_input(new_value):
                                                return len(new_value) <= 11
                                            
                                            def validate_input1(new_value):
                                                return len(new_value) <= 10
                                            
                                            def validate_input2(new_value):
                                                return len(new_value) <= 6
                                            
                                            image=Image.open(r"assets\refresh.png")
                                            reimage=image.resize((30,30))
                                            refresh_icon=ImageTk.PhotoImage(image=reimage)

                                            Label(root3,text="Get Your PIN/Secret Number",font="arial 28 bold",bg="brown",fg="white").pack(fill=X)
                                            of=Frame(root3,bg="light blue",relief="groove",borderwidth=6)
                                            of.pack()
                                            
                                            f=Frame(of,bg="light blue")
                                            f.pack()
                                            Label(f,text="Enter Your 11 Digit Account Number",font="arial 24 bold",bg="light blue",padx=20).pack(pady=15,fill=X)
                                            varr=StringVar()
                                            acn=Entry(f,textvariable=varr,font="arial 40 bold",relief="groove",width=25,bg="white",justify="center",borderwidth=4,validate="key", validatecommand=(root.register(validate_input), "%P"))
                                            acn.pack(pady=15,padx=30)
                                            
                                            f2=Frame(of,bg="light blue")
                                            f2.pack()
                                            
                                            Label(f2,text="Enter First Name:",font="arial 20 bold",bg="light blue").grid(row=0,column=0,pady=5)
                                            var1=StringVar()
                                            name=Entry(f2,textvariable=var1,font="arial 24 bold",relief="groove",width=20,justify="center",borderwidth=4,bg="white")
                                            name.grid(row=0,column=1,pady=5,padx=35)
                                            
                                            Label(f2,text="Enter Last Name:",font="arial 20 bold",bg="light blue").grid(row=1,column=0,pady=5)
                                            var2=StringVar()
                                            sname=Entry(f2,textvariable=var2,font="arial 24 bold",relief="groove",width=20,justify="center",borderwidth=4,bg="white")
                                            sname.grid(row=1,column=1,pady=5,padx=35)
                                            
                                            Label(f2,text="Enter Contact Number:",font="arial 20 bold",bg="light blue",padx=20).grid(row=2,column=0,pady=5)
                                            var3=StringVar()
                                            cont=Entry(f2,textvariable=var3,font="arial 24 bold",relief="groove",width=20,justify="center",borderwidth=4,bg="white",validate="key", validatecommand=(root.register(validate_input1), "%P"))
                                            cont.grid(row=2,column=1,pady=5,padx=35)
                                            
                                            Label(f2,text="Security Code:",font="arial 20 bold",bg="light blue",padx=20).grid(row=3,column=0,pady=15)
                                            
                                            ff=Frame(of,bg="light blue")
                                            ff.pack()
                                            
                                            captcha=Label(ff,text=get_captcha(),font="arial 20 bold",bg="light green",padx=10)
                                            captcha.grid(row=0,column=0,pady=15)
                                            Button(ff,image=refresh_icon, relief="flat", command=refresh_captcha,bg="light blue").grid(row=0,column=1,pady=15,padx=20)
                                            cv=StringVar()
                                            c_entry=Entry(ff,textvariable=cv,bg="white",relief="groove",font="arial 24 bold",width=20,justify="center",borderwidth=4,validate="key", validatecommand=(root.register(validate_input2), "%P"))
                                            c_entry.grid(row=0,column=2,pady=5,padx=55)
                                            
                                            fff=Frame(of,bg="light blue")
                                            fff.pack()
                                            def ext1():
                                                root3.destroy()
                                                new_root2.deiconify()
                                                
                                            def sub():
                                                def decode(x):
                                                    original_data=" ".join(x[i:i+8] for i in range(0,len(x),8))
                                                    data=original_data.split()
                                                    decimal_value= ''.join(chr(int(i, 2)) for i in data)
                                                    return decimal_value
                                                if acn.get() and name.get() and sname.get() and cont.get() and c_entry.get():
                                                    if acn.get().isdigit() and len(acn.get())==11:
                                                        if acn.get() == a_num.get():
                                                            if name.get().isalpha():
                                                                if sname.get().isalpha():
                                                                    if cont.get().isdigit() and len(cont.get())==10:
                                                                        if c_entry.get()==captcha["text"] and len(c_entry.get())==6:
                                                                            Name=name.get().capitalize()+" "+sname.get().capitalize()
                                                                            with open("ATM.txt","r") as f:
                                                                                data=f.readlines()
                                                                                for i  in data:
                                                                                    if i.startswith("Account Number: "+Ac):
                                                                                        a,b=i.split("; Customer Name: ")
                                                                                        c,d=b.split("; Age: ")
                                                                                        e,f=d.split("; Contact Number: ")
                                                                                        g,h=f.split("; PIN: ")
                                                                                        i,j=h.split("; Balance: ")
                                                                                        i=decode(i)
                                                                                        n1,n2=c.split(" ")
                                                                                        n1=decode(n1)
                                                                                        n2=decode(n2)
                                                                                        c=n1+" "+n2
                                                                                        g=decode(g)
                                                                                        if c==Name:
                                                                                            if g==cont.get():
                                                                                                v8=tmsg.askokcancel("Status",f"{Name} your PIN/Secret Number is: {i}")
                                                                                                if v8==True:
                                                                                                    root3.destroy()
                                                                                                    new_root2.deiconify()
                                                                                                else:
                                                                                                    root3.destroy()
                                                                                                    new_root2.deiconify()
                                                                                            else:
                                                                                                v9=tmsg.askokcancel("Status","Wrong Contact Number Entered....")
                                                                                                if v9==True:
                                                                                                    var3.set("")
                                                                                        else:
                                                                                            v7=tmsg.askokcancel("Status","Wrong Name Entered....")
                                                                                            if v7==True:
                                                                                                var1.set("")
                                                                                                var2.set("")
                                                                        else:
                                                                            v6=tmsg.askokcancel("Status","Wrong Security Code...")
                                                                            refresh_captcha()
                                                                            if v6==True:
                                                                                cv.set("")
                                                                    else:
                                                                        v5=tmsg.askokcancel("Status","Please Enter A Valid Contact Number...")
                                                                        if v5==True:
                                                                            var3.set("")
                                                                else:
                                                                    v4=tmsg.askokcancel("Status","Please Enter A Valid Last Name...")
                                                                    if v4==True:
                                                                        var2.set("")
                                                            else:
                                                                v3=tmsg.askokcancel("Status","Please Enter A Valid First Name...")
                                                                if v3==True:
                                                                    var1.set("")
                                                                        
                                                        else:
                                                            v2=tmsg.askokcancel("Status","Account Number Mismatch!...Please Enter Correct Account Number...")
                                                            if v2==True:
                                                                varr.set("")
                                                    else:
                                                        v1=tmsg.askokcancel("Status","Please Enter A Valid Account Number!...")
                                                        if v1==True:
                                                            varr.set("")
                                                else:
                                                    tmsg.askokcancel("Status","Please Fill All The Entries to Get The PIN...")
                                            Button(fff,text="Cancel",font="arial 20 bold",relief="raised",bg="Red",command=ext1,padx=5).grid(row=3,column=0,pady=30)
                                            Label(fff,text="",font="arial 20 bold",bg="light blue").grid(row=1,column=1,padx=90)
                                            Button(fff,text="Submit",bg="light green",font="arial 20 bold",relief="raised",command=sub).grid(row=3,column=2,pady=30)
                                            f3=Frame(root3,bg="brown")
                                            f3.pack(fill=X)
                                            label=Label(f3,fg="white",bg="brown",font="arial 20 bold")
                                            label.pack(fill=X)
                                            update_clock()
                                            root3.mainloop()
                                        def more():
                                            new_root2.withdraw()
                                            root3=Toplevel(new_root2)
                                            root3.geometry("1280x800")
                                            root3.minsize(1280,800)
                                            root3.maxsize(1280,800)
                                            root3.wm_iconbitmap(r"assets\atmicon.ico")
                                            root3.title("ATM MACHINE")
                                            # root3.configure(bg="black")
                                            
                                            image=Image.open(r"assets\d.jpg")
                                            photo=ImageTk.PhotoImage(image)
                                            
                                            background_label =Label(root3, image=photo)
                                            background_label.place(x=0, y=0, relwidth=1, relheight=1)

                                            
                                            def update_clock():
                                                current_time = datetime.now().strftime("Date: %Y-%m-%d & Time: %H:%M:%S")
                                                label.config(text=current_time)
                                                label.after(1000, update_clock)
                                            
                                            def validate_input(new_value):
                                                return len(new_value) <= 4
                                            
                                            f=Frame(root3,bg="light blue",relief="solid",borderwidth=4)
                                            f.pack(expand=True)
                                            
                                            Label(f,text="Enter Password",font="arial 28 bold",bg="light blue",padx=20).pack(pady=30,fill=X)
                                            pvar=StringVar()
                                            pas=Entry(f,textvariable=pvar,font="arial 40 bold",relief="solid",width=16,bg="light blue",justify="center",borderwidth=4,validate="key", validatecommand=(root.register(validate_input), "%P"),show="*")
                                            pas.pack(pady=30,padx=40)
                                            f2=Frame(f,bg="light blue")
                                            f2.pack()
                                            def sub():
                                                if pas.get():
                                                    if pas.get().isdigit and len(pas.get())==4:
                                                        if pas.get()=="0000":
                                                            def get_captcha():
                                                                str=string.ascii_letters+string.digits
                                                                captcha="".join(random.choice(str) for i in range(20))
                                                                return captcha
                                                            v1=tmsg.askyesno("Warning","Please Generate Authentication Key for Further Use....")
                                                            if v1==True:
                                                                Key=get_captcha()
                                                                v2=tmsg.askokcancel("Status","Authentication Key Generated Successfully....\nPress ok to See Authentication Key...")
                                                                if v2==True:
                                                                    root3.withdraw()
                                                                    root4=Toplevel(new_root2)
                                                                    root4.geometry("1280x800")
                                                                    root4.minsize(1280,800)
                                                                    root4.maxsize(1280,800)
                                                                    root4.configure(bg="black")
                                                                    root4.wm_iconbitmap(r"assets\atmicon.ico")
                                                                    root4.title("ATM MACHINE AUTHENTICATION KEY")
                                                                    
                                                                    def update_clock():
                                                                        current_time = datetime.now().strftime("Date: %Y-%m-%d & Time: %H:%M:%S")
                                                                        label.config(text=current_time)
                                                                        label.after(1000, update_clock)
                                                                    def validate_input(new_value):
                                                                        return len(new_value) <= 20
                                                                    
                                                                    f=Frame(root4,bg="light blue")
                                                                    f.pack(expand=True)
                                                                    Label(f,text="Authentication Key Given Below",font="arial 28 bold",bg="light blue",padx=20).pack(pady=10,fill=X)
                                                                    cap=Label(f,text=f"{Key}",font="arial 28 bold",bg="orange",padx=20)
                                                                    cap.pack(pady=10)
                                                                    Label(f,text="PLEASE COPY THE AUTHENTICATION KEY FOR FURTHER USE",font="arial 28 bold",bg="red",padx=20).pack(pady=5,fill=X)
                                                                    Label(f,text="Key Can be Copied Once After Writing in The Box Below",font="arial 20 bold",bg="yellow",padx=20).pack(pady=10,fill=X)
                                                                    
                                                                    Label(f,text="Enter Your 20 Authentication Key",font="arial 28 bold",bg="light blue",padx=20).pack(pady=10,fill=X)
                                                                    avarr=StringVar()
                                                                    ak=Entry(f,textvariable=avarr,font="arial 40 bold",relief="solid",width=24,bg="light blue",justify="center",borderwidth=4,validate="key", validatecommand=(root.register(validate_input), "%P"))
                                                                    ak.pack(pady=10)
                                                                    
                                                                    f2=Frame(f,bg="light blue")
                                                                    f2.pack()
                                                                    def ext2():
                                                                        root4.destroy()
                                                                        new_root2.deiconify()
                                                                    
                                                                    def sub1():
                                                                        if ak.get():
                                                                            if ak.get()==cap["text"] and len(ak.get())==20:
                                                                                root4.withdraw()
                                                                                new_root3=Toplevel(root4)
                                                                                new_root3.geometry("1280x800")
                                                                                new_root3.minsize(1280,800)
                                                                                new_root3.maxsize(1280,800)
                                                                                new_root3.configure(bg="lavender")
                                                                                new_root3.wm_iconbitmap(r"assets\atmicon.ico")
                                                                                new_root3.title("ATM MACHINE SPECIAL OPERATION")
                                                                                
                                                                                def update_clock():
                                                                                    current_time = datetime.now().strftime("Date: %Y-%m-%d & Time: %H:%M:%S")
                                                                                    label.config(text=current_time)
                                                                                    label.after(1000, update_clock)
                                                                                
                                                                                ff=Frame(new_root3,bg="lavender")
                                                                                ff.pack(fill=X)
                                                                                Label(ff,text="Special Operation Panel",bg="red",fg="white",font="arial 28 bold").pack(fill=X)
                                                                                Label(ff,text="",bg="lavender",font="arial 28 bold").pack(fill=X)
                                                                                                                                        
                                                                                ff1=Frame(new_root3,bg="lavender")
                                                                                ff1.pack(fill=X)
                                                                                
                                                                                def get_details():
                                                                                    new_root3.withdraw()
                                                                                    root5=Toplevel(new_root3)
                                                                                    root5.geometry("1280x800")
                                                                                    root5.minsize(1280,800)
                                                                                    root5.maxsize(1280,800)
                                                                                    root5.wm_iconbitmap(r"assets\atmicon.ico")
                                                                                    root5.title("FIND DETAILS")
                                                                                    
                                                                                    image=Image.open(r"assets\a.jpg")
                                                                                    photo=ImageTk.PhotoImage(image)
                                                                                                            
                                                                                    background_label =Label(root5, image=photo)
                                                                                    background_label.place(x=0, y=0, relwidth=1, relheight=1)
                                                                                    
                                                                                    def update_clock():
                                                                                        current_time = datetime.now().strftime("Date: %Y-%m-%d & Time: %H:%M:%S")
                                                                                        label.config(text=current_time)
                                                                                        label.after(1000, update_clock)
                                                                                    
                                                                                    def validate_input(new_value):
                                                                                        return len(new_value) <= 11
                                                                                        
                                                                                    def validate_input1(new_value):
                                                                                        return len(new_value) <= 20
                                                                                    
                                                                                    f=Frame(root5,bg="light blue",relief="solid",borderwidth=4)
                                                                                    f.pack(expand=True)
                                                                                    
                                                                                    Label(f,text="Enter Account Number",font="arial 28 bold",bg="light blue",padx=20).pack(pady=20,fill=X)
                                                                                    varrr=StringVar()
                                                                                    acn=Entry(f,textvariable=varrr,font="arial 40 bold",relief="solid",width=24,bg="light blue",justify="center",borderwidth=4,validate="key", validatecommand=(root.register(validate_input), "%P"))
                                                                                    acn.pack(pady=20,padx=20)
                                                                                    
                                                                                    Label(f,text="Enter Authentication Key",font="arial 28 bold",bg="light blue",padx=20).pack(pady=20,fill=X)
                                                                                    varr=StringVar()
                                                                                    acn_k=Entry(f,textvariable=varr,font="arial 40 bold",relief="solid",width=24,bg="light blue",justify="center",borderwidth=4,validate="key", validatecommand=(root.register(validate_input1), "%P"))
                                                                                    acn_k.pack(pady=20,padx=20)
                                                                                    f2=Frame(f,bg="light blue")
                                                                                    f2.pack()
                                                                                    
                                                                                    def ext1():
                                                                                        root5.destroy()
                                                                                        new_root3.deiconify()
                                                                                        
                                                                                    def sub():
                                                                                        def get_binary(x):
                                                                                            binary_value="".join(format(ord(i),"08b") for i in x)
                                                                                            return binary_value

                                                                                        def decode(x):
                                                                                            original_data=" ".join(x[i:i+8] for i in range(0,len(x),8))
                                                                                            data=original_data.split()
                                                                                            decimal_value= ''.join(chr(int(i, 2)) for i in data)
                                                                                            return decimal_value
                                                                                        if acn.get():
                                                                                            if acn.get().isdigit() and len(acn.get())==11:
                                                                                                acno=get_binary(acn.get())
                                                                                                if acn_k.get(): 
                                                                                                    if len(acn_k.get())==20:
                                                                                                        if acn_k.get()==ak.get():
                                                                                                            with open("ATM.txt","r") as f:
                                                                                                                data=f.readlines()
                                                                                                                for i in data:
                                                                                                                    if i.startswith("Account Number: "+acno):
                                                                                                                        i=i[len("Account Number: "):]
                                                                                                                        account_no,b=i.split("; Customer Name: ")
                                                                                                                        account_no=decode(account_no)
                                                                                                                        name,c=b.split("; Age: ")
                                                                                                                        n1,n2=name.split(" ")
                                                                                                                        n1=decode(n1)
                                                                                                                        n2=decode(n2)
                                                                                                                        name=n1+" "+n2
                                                                                                                        d,e=c.split("; Balance: ")
                                                                                                                        balance,extra=e.split(";")
                                                                                                                        balance=decode(balance)
                                                                                                                        tmsg.askokcancel("Status",f"Account Number: {account_no}; Customer Name: {name}; Balance: {balance}")
                                                                                                                        root5.destroy()
                                                                                                                        new_root3.deiconify()
                                                                                                                        break
                                                                                                                else:
                                                                                                                    tmsg.askokcancel("Status","Account Not Exist...")
                                                                                                                    root5.destroy()
                                                                                                                    new_root3.deiconify()
                                                                                                
                                                                                                        else:
                                                                                                            tmsg.askokcancel("Status","Wrong Authentication Key...")
                                                                                                            root5.destroy()
                                                                                                            root.deiconify()   
                                                                                                    else:
                                                                                                        tmsg.askokcancel("Status","Please Enter A Valid Authentication Key...")
                                                                                                        varr.set("")
                                                                                                else:
                                                                                                    tmsg.askokcancel("Status","Please Enter The Authentication Key...")
                                                                                            else:
                                                                                                tmsg.askokcancel("Status","Please Enter A Valid Account Number...")
                                                                                                varrr.set("")
                                                                                        else:
                                                                                            tmsg.askokcancel("Status","Please Enter The Account Number...")     
                                                                                    Button(f2,text="Cancel",font="arial 20 bold",relief="raised",bg="Red",command=ext1,padx=5).grid(row=0,column=0,pady=30)
                                                                                    Label(f2,text="",font="arial 20 bold",bg="light blue").grid(row=0,column=1,padx=90)
                                                                                    Button(f2,text="Submit",bg="light green",font="arial 20 bold",relief="raised",command=sub).grid(row=0,column=2,pady=30)
                                                                                    f3=Frame(f,bg="yellow")
                                                                                    f3.pack(fill=X)
                                                                                    label=Label(f3,fg="blue",bg="yellow",font="arial 20 bold")
                                                                                    label.pack(fill=X)
                                                                                    update_clock()
                                                                                    
                                                                                    root5.mainloop()
                                                                                def total_deposit():
                                                                                    new_root3.withdraw()
                                                                                    root5=Toplevel(new_root3)
                                                                                    root5.geometry("1280x800")
                                                                                    root5.minsize(1280,800)
                                                                                    root5.maxsize(1280,800)
                                                                                    root5.wm_iconbitmap(r"assets\atmicon.ico")
                                                                                    root5.title("ATM MACHINE TOTAL DEPOSIT")
                                                                                    
                                                                                    image=Image.open(r"assets\a.jpg")
                                                                                    photo=ImageTk.PhotoImage(image)
                                                                                                            
                                                                                    background_label =Label(root5, image=photo)
                                                                                    background_label.place(x=0, y=0, relwidth=1, relheight=1)
                                                                                    
                                                                                    def update_clock():
                                                                                        current_time = datetime.now().strftime("Date: %Y-%m-%d & Time: %H:%M:%S")
                                                                                        label.config(text=current_time)
                                                                                        label.after(1000, update_clock)
                                                                                        
                                                                                    def validate_input(new_value):
                                                                                        return len(new_value) <= 20
                                                                                    
                                                                                    f=Frame(root5,bg="light blue",relief="solid",borderwidth=4)
                                                                                    f.pack(expand=True)
                                                                                    
                                                                                    Label(f,text="Enter Authentication Key",font="arial 28 bold",bg="light blue",padx=20).pack(pady=30,fill=X)
                                                                                    varr=StringVar()
                                                                                    acn_k=Entry(f,textvariable=varr,font="arial 40 bold",relief="solid",width=24,bg="light blue",justify="center",borderwidth=4,validate="key", validatecommand=(root.register(validate_input), "%P"))
                                                                                    acn_k.pack(pady=30,padx=20)
                                                                                    f2=Frame(f,bg="light blue")
                                                                                    f2.pack()
                                                                                    
                                                                                    def ext1():
                                                                                        root5.destroy()
                                                                                        new_root3.deiconify()
                                                                                        
                                                                                    def sub():
                                                                                        if acn_k.get():
                                                                                            if len(acn_k.get())==20:
                                                                                                if acn_k.get()==ak.get():
                                                                                                    with open("History.txt","r") as f:
                                                                                                        data=f.readlines()
                                                                                                        dep=[]
                                                                                                        for i in data:
                                                                                                            if i.startswith("CDEPOSIT"):
                                                                                                                a,b,c,d=i.split("|")
                                                                                                                d=int(d)
                                                                                                                dep.append(d)
                                                                                                    x=sum(dep)
                                                                                                    v1=tmsg.askokcancel("Status",f"Total Rs: {x} Depositted in The ATM")
                                                                                                    if v1==True:
                                                                                                        root5.destroy()
                                                                                                        new_root3.deiconify()
                                                                                                    else:
                                                                                                        root5.destroy()
                                                                                                        new_root3.deiconify()
                                                                                                else:
                                                                                                    tmsg.askokcancel("Status","Wrong Authentication Key...")
                                                                                                    root5.destroy()
                                                                                                    root.deiconify()
                                                                                            else:
                                                                                                tmsg.askokcancel("Status","Please Enter A Valid Authentication Key...")
                                                                                                varr.set("")
                                                                                        else:
                                                                                            tmsg.askokcancel("Status","Please Enter The Authentication Key...")
                                                                                    
                                                                                    Button(f2,text="Cancel",font="arial 20 bold",relief="raised",bg="Red",command=ext1,padx=5).grid(row=0,column=0,pady=30)
                                                                                    Label(f2,text="",font="arial 20 bold",bg="light blue").grid(row=0,column=1,padx=90)
                                                                                    Button(f2,text="Submit",bg="light green",font="arial 20 bold",relief="raised",command=sub).grid(row=0,column=2,pady=30)
                                                                                    f3=Frame(f,bg="yellow")
                                                                                    f3.pack(fill=X)
                                                                                    label=Label(f3,fg="blue",bg="yellow",font="arial 20 bold")
                                                                                    label.pack(fill=X)
                                                                                    update_clock()
                                                                                    
                                                                                    root5.mainloop()
                                                                                def Atm_deposit():
                                                                                    new_root3.withdraw()
                                                                                    root5=Toplevel(new_root3)
                                                                                    root5.geometry("1280x800")
                                                                                    root5.minsize(1280,800)
                                                                                    root5.maxsize(1280,800)
                                                                                    root5.wm_iconbitmap(r"assets\atmicon.ico")
                                                                                    root5.title("ATM MACHINE CSAH DEPOSIT")
                                                                                    
                                                                                    image=Image.open(r"assets\a.jpg")
                                                                                    photo=ImageTk.PhotoImage(image)
                                                                                                            
                                                                                    background_label =Label(root5, image=photo)
                                                                                    background_label.place(x=0, y=0, relwidth=1, relheight=1)
                                                                                    
                                                                                    def update_clock():
                                                                                        current_time = datetime.now().strftime("Date: %Y-%m-%d & Time: %H:%M:%S")
                                                                                        label.config(text=current_time)
                                                                                        label.after(1000, update_clock)
                                                                                        
                                                                                    def validate_input(new_value):
                                                                                        return len(new_value) <= 20
                                                                                    
                                                                                    f=Frame(root5,bg="light blue",relief="solid",borderwidth=4)
                                                                                    f.pack(expand=True)
                                                                                    
                                                                                    Label(f,text="Enter Authentication Key",font="arial 28 bold",bg="light blue",padx=20).pack(pady=30,fill=X)
                                                                                    varr=StringVar()
                                                                                    acn_k=Entry(f,textvariable=varr,font="arial 40 bold",relief="solid",width=24,bg="light blue",justify="center",borderwidth=4,validate="key", validatecommand=(root.register(validate_input), "%P"))
                                                                                    acn_k.pack(pady=30,padx=20)
                                                                                    f2=Frame(f,bg="light blue")
                                                                                    f2.pack()
                                                                                    
                                                                                    def ext1():
                                                                                        root5.destroy()
                                                                                        new_root3.deiconify()
                                                                                        
                                                                                    def sub():
                                                                                        if acn_k.get():
                                                                                            if len(acn_k.get())==20:
                                                                                                if acn_k.get()==ak.get():
                                                                                                    root5.withdraw()
                                                                                                    root6=Toplevel(root5)
                                                                                                    root6.geometry("1280x800")
                                                                                                    root6.minsize(1280,800)
                                                                                                    root6.maxsize(1280,800)
                                                                                                    root6.wm_iconbitmap(r"assets\atmicon.ico")
                                                                                                    root6.title("ATM MACHINE CSAH DEPOSIT")
                                                                                                    
                                                                                                    image=Image.open(r"assets\d.jpg")
                                                                                                    photo=ImageTk.PhotoImage(image)
                                                                                                                            
                                                                                                    background_label =Label(root6, image=photo)
                                                                                                    background_label.place(x=0, y=0, relwidth=1, relheight=1)
                                                                                                    
                                                                                                    def update_clock():
                                                                                                        current_time = datetime.now().strftime("Date: %Y-%m-%d & Time: %H:%M:%S")
                                                                                                        label.config(text=current_time)
                                                                                                        label.after(1000, update_clock)
                                                                                                        
                                                                                                    def validate_input(new_value):
                                                                                                        return len(new_value) <= 11
                                                                                                    
                                                                                                    f=Frame(root6,bg="light blue",relief="solid",borderwidth=4)
                                                                                                    f.pack(expand=True)
                                                                                                    
                                                                                                    Label(f,text="Enter Official Account Number",font="arial 28 bold",bg="light blue",padx=20).pack(pady=30,fill=X)
                                                                                                    var=StringVar()
                                                                                                    acn=Entry(f,textvariable=var,font="arial 40 bold",relief="solid",width=24,bg="light blue",justify="center",borderwidth=4,validate="key", validatecommand=(root.register(validate_input), "%P"))
                                                                                                    acn.pack(pady=30,padx=20)
                                                                                                    f2=Frame(f,bg="light blue")
                                                                                                    f2.pack()
                                                                                                    def ext2():
                                                                                                        root6.destroy()
                                                                                                        new_root3.deiconify()
                                                                                                    def sub1():
                                                                                                        if acn.get():
                                                                                                            if acn.get().isdigit() and len(acn.get())==11:
                                                                                                                if acn.get()==a_num.get():
                                                                                                                    root6.withdraw()
                                                                                                                    root7=Toplevel(root6)
                                                                                                                    root7.geometry("1280x800")
                                                                                                                    root7.minsize(1280,800)
                                                                                                                    root7.maxsize(1280,800)
                                                                                                                    root7.wm_iconbitmap(r"assets\atmicon.ico")
                                                                                                                    root7.title("ATM MACHINE CSAH DEPOSIT")               
                                                                                                                    
                                                                                                                    image=Image.open(r"assets\c.jpg")
                                                                                                                    photo=ImageTk.PhotoImage(image)
                                                                                                                                            
                                                                                                                    background_label =Label(root7, image=photo)
                                                                                                                    background_label.place(x=0, y=0, relwidth=1, relheight=1)
                                                                                                                    
                                                                                                                    def update_clock():
                                                                                                                        current_time = datetime.now().strftime("Date: %Y-%m-%d & Time: %H:%M:%S")
                                                                                                                        label.config(text=current_time)
                                                                                                                        label.after(1000, update_clock)
                                                                                                                        
                                                                                                                    def validate_input(new_value):
                                                                                                                        return len(new_value) <= 11
                                                                                                                    
                                                                                                                    f=Frame(root7,bg="light blue",relief="solid",borderwidth=4)
                                                                                                                    f.pack(expand=True)
                                                                                                                    
                                                                                                                    Label(f,text="Enter Amount To Deposit",font="arial 28 bold",bg="light blue",padx=20).pack(pady=30,fill=X)
                                                                                                                    vaar=StringVar()
                                                                                                                    a_n=Entry(f,textvariable=vaar,font="arial 40 bold",relief="solid",width=24,bg="light blue",justify="center",borderwidth=4,validate="key", validatecommand=(root.register(validate_input), "%P"))
                                                                                                                    a_n.pack(pady=30,padx=20)
                                                                                                                    f2=Frame(f,bg="light blue")
                                                                                                                    f2.pack()
                                                                                                                    def ext3():
                                                                                                                        root7.destroy()
                                                                                                                        new_root3.deiconify()
                                                                                                                    def sub2():
                                                                                                                        def get_binary(x):
                                                                                                                            binary_value="".join(format(ord(i),"08b") for i in x)
                                                                                                                            return binary_value
                                                                                                                        acco=get_binary(acn.get())
                                                                                                                        if a_n.get():
                                                                                                                            if a_n.get().isdigit() and int(a_n.get())>0:
                                                                                                                                pygame.init()
                                                                                                                                audio_path = r"assets\machine sound.mp3"
                                                                                                                                pygame.mixer.music.load(audio_path)
                                                                                                                                pygame.mixer.music.play()
                                                                                                                                # tmsg.askokcancel("Status","Please Wait!...Counting Is Under Progress...")
                                                                                                                                pygame.time.delay(6000)
                                                                                                                                pygame.quit()
                                                                                                                                today = datetime.today().strftime("%Y-%m-%d")
                                                                                                                                with open("History.txt","r") as f:
                                                                                                                                    data=f.readlines()
                                                                                                                                    if len(data)==0:
                                                                                                                                        with open("History.txt","w") as f:
                                                                                                                                            f.write(f"ABALANCE|{acco}|{today}|{a_n.get()}\n")
                                                                                                                                        tmsg.askokcancel("Status",f"Amount Of Rs: {a_n.get()} Depositted In The ATM Successfully...")
                                                                                                                                        root7.destroy()
                                                                                                                                        new_root3.deiconify()
                                                                                                                                    else:
                                                                                                                                        with open("History.txt","a") as f:
                                                                                                                                            f.write(f"ATM_CASH_DEPOSIT-{acco}-{today}-{a_n.get()}\n")
                                                                                                                                        with open("History.txt","r") as f:
                                                                                                                                            data=f.readlines()
                                                                                                                                            for index, i in enumerate(data):
                                                                                                                                                if i.startswith("ABALANCE"):
                                                                                                                                                    a,b,c,d=i.split("|")
                                                                                                                                                    d=int(d)
                                                                                                                                                    d=d+int(a_n.get())
                                                                                                                                                    d=str(d)
                                                                                                                                                    data[index]=a+"|"+b+"|"+today+"|"+d+"\n" 
                                                                                                                                        with open("History.txt","w") as f:
                                                                                                                                            f.writelines(data)
                                                                                                                                        tmsg.askokcancel("Status",f"Amount Of Rs: {a_n.get()} Depositted In The ATM Successfully...")
                                                                                                                                        root7.destroy()
                                                                                                                                        new_root3.deiconify()
                                                                                                                            else:
                                                                                                                                tmsg.askokcancel("Status","Please Enter A Valid Amount...")
                                                                                                                                vaar.set("")
                                                                                                                        else:
                                                                                                                            tmsg.askokcancel("Status","Please Enter The Amount...")
                                                                                                                    Button(f2,text="Cancel",font="arial 20 bold",relief="raised",bg="Red",command=ext3,padx=5).grid(row=0,column=0,pady=30)
                                                                                                                    Label(f2,text="",font="arial 20 bold",bg="light blue").grid(row=0,column=1,padx=90)
                                                                                                                    Button(f2,text="Submit",bg="light green",font="arial 20 bold",relief="raised",command=sub2).grid(row=0,column=2,pady=30)
                                                                                                                    f3=Frame(f,bg="yellow")
                                                                                                                    f3.pack(fill=X)
                                                                                                                    label=Label(f3,fg="blue",bg="yellow",font="arial 20 bold")
                                                                                                                    label.pack(fill=X)
                                                                                                                    update_clock()
                                                                                                                    root7.mainloop()
                                                                                                                else:
                                                                                                                    tmsg.askokcancel("Status","Wrong account Number...")
                                                                                                                    root6.destroy()
                                                                                                                    new_root3.deiconify()
                                                                                                            else:
                                                                                                                tmsg.askokcancel("Status","Please Enter A Valid Account Number...")
                                                                                                                var.set("")
                                                                                                        else:
                                                                                                            tmsg.askokcancel("Status","Please Enter The Account Number...")
                                                                                                    Button(f2,text="Cancel",font="arial 20 bold",relief="raised",bg="Red",command=ext2,padx=5).grid(row=0,column=0,pady=30)
                                                                                                    Label(f2,text="",font="arial 20 bold",bg="light blue").grid(row=0,column=1,padx=90)
                                                                                                    Button(f2,text="Submit",bg="light green",font="arial 20 bold",relief="raised",command=sub1).grid(row=0,column=2,pady=30)
                                                                                                    f3=Frame(f,bg="yellow")
                                                                                                    f3.pack(fill=X)
                                                                                                    label=Label(f3,fg="blue",bg="yellow",font="arial 20 bold")
                                                                                                    label.pack(fill=X)
                                                                                                    update_clock()
                                                                                                    root6.mainloop()
                                                                                                else:
                                                                                                    tmsg.askokcancel("Status","Wrong Authentication Key...")
                                                                                                    root5.destroy()
                                                                                                    root.deiconify()
                                                                                            else:
                                                                                                tmsg.askokcancel("Status","Please Enter A Valid Authentication Key...")
                                                                                                varr.set("")
                                                                                        else:
                                                                                            tmsg.askokcancel("Status","Please Enter The Authentication Key...")
                                                                                    Button(f2,text="Cancel",font="arial 20 bold",relief="raised",bg="Red",command=ext1,padx=5).grid(row=0,column=0,pady=30)
                                                                                    Label(f2,text="",font="arial 20 bold",bg="light blue").grid(row=0,column=1,padx=90)
                                                                                    Button(f2,text="Submit",bg="light green",font="arial 20 bold",relief="raised",command=sub).grid(row=0,column=2,pady=30)
                                                                                    f3=Frame(f,bg="yellow")
                                                                                    f3.pack(fill=X)
                                                                                    label=Label(f3,fg="blue",bg="yellow",font="arial 20 bold")
                                                                                    label.pack(fill=X)
                                                                                    update_clock()
                                                                                    root5.mainloop()
                                                                                def total_withdraw():
                                                                                    new_root3.withdraw()
                                                                                    root5=Toplevel(new_root3)
                                                                                    root5.geometry("1280x800")
                                                                                    root5.minsize(1280,800)
                                                                                    root5.maxsize(1280,800)
                                                                                    root5.wm_iconbitmap(r"assets\atmicon.ico")
                                                                                    root5.title("ATM MACHINE TOTAL WITHDRAW")
                                                                                    
                                                                                    image=Image.open(r"assets\a.jpg")
                                                                                    photo=ImageTk.PhotoImage(image)
                                                                                                            
                                                                                    background_label =Label(root5, image=photo)
                                                                                    background_label.place(x=0, y=0, relwidth=1, relheight=1)
                                                                                    
                                                                                    def update_clock():
                                                                                        current_time = datetime.now().strftime("Date: %Y-%m-%d & Time: %H:%M:%S")
                                                                                        label.config(text=current_time)
                                                                                        label.after(1000, update_clock)
                                                                                        
                                                                                    def validate_input(new_value):
                                                                                        return len(new_value) <= 20
                                                                                    
                                                                                    f=Frame(root5,bg="light blue",relief="solid",borderwidth=4)
                                                                                    f.pack(expand=True)
                                                                                    
                                                                                    Label(f,text="Enter Authentication Key",font="arial 28 bold",bg="light blue",padx=20).pack(pady=30,fill=X)
                                                                                    varr=StringVar()
                                                                                    acn_k=Entry(f,textvariable=varr,font="arial 40 bold",relief="solid",width=24,bg="light blue",justify="center",borderwidth=4,validate="key", validatecommand=(root.register(validate_input), "%P"))
                                                                                    acn_k.pack(pady=30,padx=20)
                                                                                    f2=Frame(f,bg="light blue")
                                                                                    f2.pack()
                                                                                    
                                                                                    def ext1():
                                                                                        root5.destroy()
                                                                                        new_root3.deiconify()
                                                                                        
                                                                                    def sub():
                                                                                        if acn_k.get():
                                                                                            if len(acn_k.get())==20:
                                                                                                if acn_k.get()==ak.get():
                                                                                                    with open("History.txt","r") as f:
                                                                                                        data=f.readlines()
                                                                                                        dep=[]
                                                                                                        for i in data:
                                                                                                            if i.startswith("WITHDRAW"):
                                                                                                                a,b,c,d=i.split("|")
                                                                                                                d=int(d)
                                                                                                                dep.append(d)
                                                                                                    x=sum(dep)
                                                                                                    v1=tmsg.askokcancel("Status",f"Total Rs: {x} Withdrawn from The ATM")
                                                                                                    if v1==True:
                                                                                                        root5.destroy()
                                                                                                        new_root3.deiconify()
                                                                                                    else:
                                                                                                        root5.destroy()
                                                                                                        new_root3.deiconify()
                                                                                                else:
                                                                                                    tmsg.askokcancel("Status","Wrong Authentication Key...")
                                                                                                    root5.destroy()
                                                                                                    root.deiconify()
                                                                                            else:
                                                                                                tmsg.askokcancel("Status","Please Enter A Valid Authentication Key...")
                                                                                                varr.set("")
                                                                                        else:
                                                                                            tmsg.askokcancel("Status","Please Enter The Authentication Key...")
                                                                                    
                                                                                    Button(f2,text="Cancel",font="arial 20 bold",relief="raised",bg="Red",command=ext1,padx=5).grid(row=0,column=0,pady=30)
                                                                                    Label(f2,text="",font="arial 20 bold",bg="light blue").grid(row=0,column=1,padx=90)
                                                                                    Button(f2,text="Submit",bg="light green",font="arial 20 bold",relief="raised",command=sub).grid(row=0,column=2,pady=30)
                                                                                    f3=Frame(f,bg="yellow")
                                                                                    f3.pack(fill=X)
                                                                                    label=Label(f3,fg="blue",bg="yellow",font="arial 20 bold")
                                                                                    label.pack(fill=X)
                                                                                    update_clock()
                                                                                    
                                                                                    root5.mainloop()
                                                                                def Atm_balance():
                                                                                    new_root3.withdraw()
                                                                                    root5=Toplevel(new_root3)
                                                                                    root5.geometry("1280x800")
                                                                                    root5.minsize(1280,800)
                                                                                    root5.maxsize(1280,800)
                                                                                    root5.wm_iconbitmap(r"assets\atmicon.ico")
                                                                                    root5.title("ATM MACHINE BALANCE")
                                                                                    
                                                                                    image=Image.open(r"assets\a.jpg")
                                                                                    photo=ImageTk.PhotoImage(image)
                                                                                                            
                                                                                    background_label =Label(root5, image=photo)
                                                                                    background_label.place(x=0, y=0, relwidth=1, relheight=1)
                                                                                    
                                                                                    def update_clock():
                                                                                        current_time = datetime.now().strftime("Date: %Y-%m-%d & Time: %H:%M:%S")
                                                                                        label.config(text=current_time)
                                                                                        label.after(1000, update_clock)
                                                                                        
                                                                                    def validate_input(new_value):
                                                                                        return len(new_value) <= 20
                                                                                    
                                                                                    f=Frame(root5,bg="light blue",relief="solid",borderwidth=4)
                                                                                    f.pack(expand=True)
                                                                                    
                                                                                    Label(f,text="Enter Authentication Key",font="arial 28 bold",bg="light blue",padx=20).pack(pady=30,fill=X)
                                                                                    varr=StringVar()
                                                                                    acn_k=Entry(f,textvariable=varr,font="arial 40 bold",relief="solid",width=24,bg="light blue",justify="center",borderwidth=4,validate="key", validatecommand=(root.register(validate_input), "%P"))
                                                                                    acn_k.pack(pady=30,padx=20)
                                                                                    f2=Frame(f,bg="light blue")
                                                                                    f2.pack()
                                                                                    
                                                                                    def ext1():
                                                                                        root5.destroy()
                                                                                        new_root3.deiconify()
                                                                                        
                                                                                    def sub():
                                                                                        if acn_k.get():
                                                                                            if len(acn_k.get())==20:
                                                                                                if acn_k.get()==ak.get():
                                                                                                    with open("History.txt","r") as f:
                                                                                                        data=f.readlines()
                                                                                                        if len(data)>0:
                                                                                                            for i in data:
                                                                                                                if i.startswith("ABALANCE"):
                                                                                                                    a,b,c,d=i.split("|")
                                                                                                            v1=tmsg.askokcancel("Status",f"Available Balance in The ATM Rs: {d}")
                                                                                                            if v1==True:
                                                                                                                root5.destroy()
                                                                                                                new_root3.deiconify()
                                                                                                            else:
                                                                                                                root5.destroy()
                                                                                                                new_root3.deiconify()
                                                                                                        else:
                                                                                                            tmsg.askokcancel("Status","Please Add CASH In The ATM!...")
                                                                                                            root5.destroy()
                                                                                                            new_root3.deiconify()
                                                                                                else:
                                                                                                    tmsg.askokcancel("Status","Wrong Authentication Key...")
                                                                                                    root5.destroy()
                                                                                                    root.deiconify()
                                                                                            else:
                                                                                                tmsg.askokcancel("Status","Please Enter A Valid Authentication Key...")
                                                                                                varr.set("")
                                                                                        else:
                                                                                            tmsg.askokcancel("Status","Please Enter The Authentication Key...")
                                                                                    
                                                                                    Button(f2,text="Cancel",font="arial 20 bold",relief="raised",bg="Red",command=ext1,padx=5).grid(row=0,column=0,pady=30)
                                                                                    Label(f2,text="",font="arial 20 bold",bg="light blue").grid(row=0,column=1,padx=90)
                                                                                    Button(f2,text="Submit",bg="light green",font="arial 20 bold",relief="raised",command=sub).grid(row=0,column=2,pady=30)
                                                                                    f3=Frame(f,bg="yellow")
                                                                                    f3.pack(fill=X)
                                                                                    label=Label(f3,fg="blue",bg="yellow",font="arial 20 bold")
                                                                                    label.pack(fill=X)
                                                                                    update_clock()
                                                                                    
                                                                                    root5.mainloop()
                                                                                def ext3():
                                                                                    new_root3.destroy()
                                                                                    root.deiconify()
                                                                                def td():
                                                                                    new_root3.withdraw()
                                                                                    root5=Toplevel(new_root3)
                                                                                    root5.geometry("1280x800")
                                                                                    root5.minsize(1280,800)
                                                                                    root5.maxsize(1280,800)
                                                                                    root5.wm_iconbitmap(r"assets\atmicon.ico")
                                                                                    root5.title("ATM MACHINE TODAY'S DEPOSIT")
                                                                                    
                                                                                    image=Image.open(r"assets\a.jpg")
                                                                                    photo=ImageTk.PhotoImage(image)
                                                                                                            
                                                                                    background_label =Label(root5, image=photo)
                                                                                    background_label.place(x=0, y=0, relwidth=1, relheight=1)
                                                                                    
                                                                                    def update_clock():
                                                                                        current_time = datetime.now().strftime("Date: %Y-%m-%d & Time: %H:%M:%S")
                                                                                        label.config(text=current_time)
                                                                                        label.after(1000, update_clock)
                                                                                        
                                                                                    def validate_input(new_value):
                                                                                        return len(new_value) <= 20
                                                                                    
                                                                                    f=Frame(root5,bg="light blue",relief="solid",borderwidth=4)
                                                                                    f.pack(expand=True)
                                                                                    
                                                                                    Label(f,text="Enter Authentication Key",font="arial 28 bold",bg="light blue",padx=20).pack(pady=30,fill=X)
                                                                                    varr=StringVar()
                                                                                    acn_k=Entry(f,textvariable=varr,font="arial 40 bold",relief="solid",width=24,bg="light blue",justify="center",borderwidth=4,validate="key", validatecommand=(root.register(validate_input), "%P"))
                                                                                    acn_k.pack(pady=30,padx=20)
                                                                                    f2=Frame(f,bg="light blue")
                                                                                    f2.pack()
                                                                                    
                                                                                    def ext1():
                                                                                        root5.destroy()
                                                                                        new_root3.deiconify()
                                                                                        
                                                                                    def sub():
                                                                                        if acn_k.get():
                                                                                            if len(acn_k.get())==20:
                                                                                                if acn_k.get()==ak.get():
                                                                                                    today = datetime.today().strftime("%Y-%m-%d")
                                                                                                    with open("History.txt","r") as f:
                                                                                                        data=f.readlines()
                                                                                                        dep=[]
                                                                                                        for i in data:
                                                                                                            if i.startswith("CDEPOSIT"):
                                                                                                                a,b,c,d=i.split("|")
                                                                                                                d=int(d)
                                                                                                                if c==today:
                                                                                                                    dep.append(d)
                                                                                                    x=sum(dep)
                                                                                                    v1=tmsg.askokcancel("Status",f"Total Rs: {x} Depositted In The ATM On {today}")
                                                                                                    if v1==True:
                                                                                                        root5.destroy()
                                                                                                        new_root3.deiconify()
                                                                                                    else:
                                                                                                        root5.destroy()
                                                                                                        new_root3.deiconify()
                                                                                                else:
                                                                                                    tmsg.askokcancel("Status","Wrong Authentication Key...")
                                                                                                    root5.destroy()
                                                                                                    root.deiconify()
                                                                                            else:
                                                                                                tmsg.askokcancel("Status","Please Enter A Valid Authentication Key...")
                                                                                                varr.set("")
                                                                                        else:
                                                                                            tmsg.askokcancel("Status","Please Enter The Authentication Key...")
                                                                                    
                                                                                    Button(f2,text="Cancel",font="arial 20 bold",relief="raised",bg="Red",command=ext1,padx=5).grid(row=0,column=0,pady=30)
                                                                                    Label(f2,text="",font="arial 20 bold",bg="light blue").grid(row=0,column=1,padx=90)
                                                                                    Button(f2,text="Submit",bg="light green",font="arial 20 bold",relief="raised",command=sub).grid(row=0,column=2,pady=30)
                                                                                    f3=Frame(f,bg="yellow")
                                                                                    f3.pack(fill=X)
                                                                                    label=Label(f3,fg="blue",bg="yellow",font="arial 20 bold")
                                                                                    label.pack(fill=X)
                                                                                    update_clock()
                                                                                    
                                                                                    root5.mainloop()
                                                                                def tw():
                                                                                    new_root3.withdraw()
                                                                                    root5=Toplevel(new_root3)
                                                                                    root5.geometry("1280x800")
                                                                                    root5.minsize(1280,800)
                                                                                    root5.maxsize(1280,800)
                                                                                    root5.wm_iconbitmap(r"assets\atmicon.ico")
                                                                                    root5.title("ATM MACHINE TODAY'S WITHDRAW")
                                                                                    
                                                                                    image=Image.open(r"assets\a.jpg")
                                                                                    photo=ImageTk.PhotoImage(image)
                                                                                                            
                                                                                    background_label =Label(root5, image=photo)
                                                                                    background_label.place(x=0, y=0, relwidth=1, relheight=1)
                                                                                    
                                                                                    def update_clock():
                                                                                        current_time = datetime.now().strftime("Date: %Y-%m-%d & Time: %H:%M:%S")
                                                                                        label.config(text=current_time)
                                                                                        label.after(1000, update_clock)
                                                                                        
                                                                                    def validate_input(new_value):
                                                                                        return len(new_value) <= 20
                                                                                    
                                                                                    f=Frame(root5,bg="light blue",relief="solid",borderwidth=4)
                                                                                    f.pack(expand=True)
                                                                                    
                                                                                    Label(f,text="Enter Authentication Key",font="arial 28 bold",bg="light blue",padx=20).pack(pady=30,fill=X)
                                                                                    varr=StringVar()
                                                                                    acn_k=Entry(f,textvariable=varr,font="arial 40 bold",relief="solid",width=24,bg="light blue",justify="center",borderwidth=4,validate="key", validatecommand=(root.register(validate_input), "%P"))
                                                                                    acn_k.pack(pady=30,padx=20)
                                                                                    f2=Frame(f,bg="light blue")
                                                                                    f2.pack()
                                                                                    
                                                                                    def ext1():
                                                                                        root5.destroy()
                                                                                        new_root3.deiconify()
                                                                                        
                                                                                    def sub():
                                                                                        if acn_k.get():
                                                                                            if len(acn_k.get())==20:
                                                                                                if acn_k.get()==ak.get():
                                                                                                    today = datetime.today().strftime("%Y-%m-%d")
                                                                                                    with open("History.txt","r") as f:
                                                                                                        data=f.readlines()
                                                                                                        dep=[]
                                                                                                        for i in data:
                                                                                                            if i.startswith("WITHDRAW"):
                                                                                                                a,b,c,d=i.split("|")
                                                                                                                d=int(d)
                                                                                                                if c==today:
                                                                                                                    dep.append(d)
                                                                                                    x=sum(dep)
                                                                                                    v1=tmsg.askokcancel("Status",f"Total Rs: {x} Withdrawn from The ATM on {today}")
                                                                                                    if v1==True:
                                                                                                        root5.destroy()
                                                                                                        new_root3.deiconify()
                                                                                                    else:
                                                                                                        root5.destroy()
                                                                                                        new_root3.deiconify()
                                                                                                else:
                                                                                                    tmsg.askokcancel("Status","Wrong Authentication Key...")
                                                                                                    root5.destroy()
                                                                                                    root.deiconify()
                                                                                            else:
                                                                                                tmsg.askokcancel("Status","Please Enter A Valid Authentication Key...")
                                                                                                varr.set("")
                                                                                        else:
                                                                                            tmsg.askokcancel("Status","Please Enter The Authentication Key...")
                                                                                    
                                                                                    Button(f2,text="Cancel",font="arial 20 bold",relief="raised",bg="Red",command=ext1,padx=5).grid(row=0,column=0,pady=30)
                                                                                    Label(f2,text="",font="arial 20 bold",bg="light blue").grid(row=0,column=1,padx=90)
                                                                                    Button(f2,text="Submit",bg="light green",font="arial 20 bold",relief="raised",command=sub).grid(row=0,column=2,pady=30)
                                                                                    f3=Frame(f,bg="yellow")
                                                                                    f3.pack(fill=X)
                                                                                    label=Label(f3,fg="blue",bg="yellow",font="arial 20 bold")
                                                                                    label.pack(fill=X)
                                                                                    update_clock()
                                                                                    
                                                                                    root5.mainloop()
                                                                                Button(ff1,text="Get Any Details",bg="light green",font="arial 28 bold",relief="raised",padx=22,command=get_details).grid(row=0,column=0,pady=35)
                                                                                Label(ff1,text="",bg="lavender",font="arial 28 bold").grid(row=0,column=1,padx=292,pady=35)
                                                                                Button(ff1,text="Total Deposit",bg="light green",font="arial 28 bold",relief="raised",padx=34,command=total_deposit).grid(row=0,column=2,pady=35)
                                                                                Button(ff1,text="ATM Deposit",bg="light green",font="arial 28 bold",relief="raised",padx=45,command=Atm_deposit).grid(row=1,column=0,pady=35)
                                                                                Button(ff1,text="Total Withdraw",bg="light green",font="arial 28 bold",relief="raised",padx=19,command=total_withdraw).grid(row=1,column=2,pady=35)
                                                                                Button(ff1,text="ATM Balance",bg="light green",font="arial 28 bold",relief="raised",padx=41,command=Atm_balance).grid(row=2,column=0,pady=35)
                                                                                Button(ff1,text="Exit",bg="light green",font="arial 28 bold",relief="raised",padx=119,command=ext3).grid(row=2,column=2,pady=35)
                                                                                Button(ff1,text="Today Deposit",bg="light green",font="arial 28 bold",relief="raised",padx=30,command=td).grid(row=3,column=0,pady=37)
                                                                                Button(ff1,text="Today Withdraw",bg="light green",font="arial 28 bold",relief="raised",padx=15,command=tw).grid(row=3,column=2,pady=37)

                                                                            else:
                                                                                tmsg.askokcancel("Status","Please Enter A Valid Authentication Key!...")
                                                                                avarr.set("")
                                                                        else:
                                                                            tmsg.askokcancel("Status","Please Enter The Authentication Key...")

                        
                                                                    Button(f2,text="Cancel",font="arial 20 bold",relief="raised",bg="Red",command=ext2,padx=5).grid(row=0,column=0,pady=30)
                                                                    Label(f2,text="",font="arial 20 bold",bg="light blue").grid(row=0,column=1,padx=90)
                                                                    Button(f2,text="Submit",bg="light green",font="arial 20 bold",relief="raised",command=sub1).grid(row=0,column=2,pady=30)
                                                                    f3=Frame(f,bg="yellow")
                                                                    f3.pack(fill=X)
                                                                    label=Label(f3,fg="blue",bg="yellow",font="arial 20 bold")
                                                                    label.pack(fill=X)
                                                                    update_clock()
                                                                    root4.mainloop()
                                                                
                                                        else:
                                                            tmsg.askokcancel("Status","Wrong Password!...")
                                                            root3.destroy()
                                                            new_root2.deiconify()
                                                    else:
                                                        tmsg.askokcancel("Status","Please Enter A Valid Password!...")
                                                        pvar.set("")
                                                else:
                                                    tmsg.askokcancel("Status","Please Enter The Password!...")
                                            def ext1():
                                                root3.destroy()
                                                new_root2.deiconify()
                                            Button(f2,text="Cancel",font="arial 20 bold",relief="raised",bg="Red",command=ext1,padx=5).grid(row=0,column=0,pady=30)
                                            Label(f2,text="",font="arial 20 bold",bg="light blue").grid(row=0,column=1,padx=90)
                                            Button(f2,text="Submit",bg="light green",font="arial 20 bold",relief="raised",command=sub).grid(row=0,column=2,pady=30)
                                            f3=Frame(f,bg="yellow")
                                            f3.pack(fill=X)
                                            label=Label(f3,fg="blue",bg="yellow",font="arial 20 bold")
                                            label.pack(fill=X)
                                            update_clock()
                                            root3.mainloop()
                                            
                                        Label(f1,text="",bg="lavender",font="arial 28 bold").grid(row=0,column=1)
                                        Label(f1,text="",bg="lavender",font="arial 28 bold").grid(row=0,column=1,padx=331)
                                        Button(f1,text="Cash Deposit",bg="light green",font="arial 28 bold",relief="raised",padx=18,command=deposit,state=s).grid(row=0,column=2)
                                        Button(f1,text="Balance Inquiry",bg="light green",font="arial 28 bold",relief="raised",padx=5,command=balance,state=s).grid(row=1,column=0)
                                        Button(f1,text="Cash Withdraw",bg="light green",font="arial 28 bold",relief="raised",command=withdraw,state=s).grid(row=2,column=2)
                                        Button(f1,text="Change Pin",bg="light green",font="arial 28 bold",relief="raised",padx=40,command=pin_change,state=s).grid(row=3,column=0)
                                        Button(f1,text="Exit",bg="light green",font="arial 28 bold",relief="raised",padx=100,command=ext).grid(row=4,column=2)
                                        Button(f1,text="Forget Pin",bg="light green",font="arial 28 bold",relief="raised",padx=51,command=forget_pin,state=s).grid(row=5,column=0)
                                        Button(f1,text="More",bg="light green",font="arial 28 bold",relief="raised",padx=90,state=st,command=more).grid(row=6,column=2,pady=26)
                                        
                                        f2=Frame(new_root2,bg="yellow")
                                        f2.pack(fill=X)
                                        label=Label(f2,fg="blue",bg="yellow",font="arial 20 bold")
                                        label.pack(fill=X)
                                        update_clock()
                                        new_root2.after(300000,hide_message_box)
                                        new_root2.mainloop()
                                else:
                                    val=tmsg.askokcancel("Status","This Account Number is not Exist!...")
                                    if val==True:
                                        var.set("")
                                    else:
                                        new_root.destroy()
                                        root.deiconify()
                                    
    def end1():
        new_root.destroy()
        root.deiconify()
    fr1=Frame(new_root,bg="light blue",relief=SOLID)
    fr1.pack(expand=True)
    l=Label(fr1,text="Enter Account Number",bg="light blue",font="arial 28 bold")
    l.pack(pady=30)
    var=StringVar()
    a_num=Entry(fr1,textvariable=var,font="arial 40 bold",relief="solid",width=20,bg="light blue",justify="center",borderwidth=4,validate="key", validatecommand=(root.register(validate_input), "%P"))
    a_num.pack(pady=30,padx=30)
    
    fr2=Frame(fr1,bg="light blue")
    fr2.pack()
    b2=Button(fr2,text="Cancel",font="arial 20 bold",relief="raised",bg="Red",command=end1,padx=5)
    b2.grid(row=0,column=0,pady=30)
    Label(fr2,text="",font="arial 20 bold",bg="light blue").grid(row=0,column=1,padx=90)
    b=Button(fr2,text="Submit",bg="light green",font="arial 20 bold",relief="raised",command=details)
    b.grid(row=0,column=2,pady=30)
    
    fr3=Frame(fr1,bg="yellow")
    fr3.pack(fill=X)
    label=Label(fr3,fg="blue",bg="yellow",font="arial 20 bold")
    label.pack(fill=X)
    update_clock()
    new_root.mainloop()
def end():
    x=tmsg.askyesno("Status","Do You Want To Exit?")
    if x==True:
        root.withdraw()
        root1=Toplevel(root)
        root1.geometry("1280x800")
        root1.minsize(1280,800)
        root1.maxsize(1280,800)
        root1.configure(bg="lavender")
        root1.wm_iconbitmap(r"assets\atmicon.ico")
        root1.title("ATM MACHINE")
        
        def update_clock():
            current_time = datetime.now().strftime("Date: %Y-%m-%d & Time: %H:%M:%S")
            label.config(text=current_time)
            label.after(1000, update_clock)  # Update every 1000 milliseconds (1 second)
        
        def validate_input(new_value):
            return len(new_value) <= 4
        
        def return_to_root():
            root1.destroy()
            root.deiconify()
            tmsg.showinfo("Status","Session Time-out!...")
            
        image=Image.open(r"assets\a.jpg")
        photo=ImageTk.PhotoImage(image)
                                                                                                            
        background_label =Label(root1, image=photo)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
                                                                                        
        f=Frame(root1,bg="light blue",relief="solid",borderwidth=4)
        f.pack(expand=True)
        Label(f,text="Enter ATM Password",font="arial 28 bold",bg="light blue",padx=20).pack(pady=30,fill=X)
        varr=StringVar()
        acn_k=Entry(f,textvariable=varr,font="arial 40 bold",relief="solid",width=16,bg="light blue",justify="center",borderwidth=4,validate="key", validatecommand=(root.register(validate_input), "%P"),show="*",fg="red")
        acn_k.pack(pady=30,padx=20)
        f2=Frame(f,bg="light blue")
        f2.pack()
                                                                                    
        def ext1():
            root1.destroy()
            root.deiconify()
                                                                                        
        def sub():
            if acn_k.get():
                if acn_k.get().isdigit() and len(acn_k.get())==4:
                    if acn_k.get()=="0000":
                        root.destroy()
                    else:
                        tmsg.askokcancel("Status","Wrong Password!...")
                        root1.destroy()
                        root.deiconify()
                else:
                    tmsg.askokcancel("Status","Please Enter A Valid Password!...")
                    varr.set("")
            else:
                tmsg.askokcancel("Status","Please Enter The Password!...")
            
        Button(f2,text="Cancel",font="arial 20 bold",relief="raised",bg="Red",command=ext1,padx=5).grid(row=0,column=0,pady=30)
        Label(f2,text="",font="arial 20 bold",bg="light blue").grid(row=0,column=1,padx=90)
        Button(f2,text="Submit",bg="light green",font="arial 20 bold",relief="raised",command=sub).grid(row=0,column=2,pady=30)
        f3=Frame(f,bg="yellow")
        f3.pack(fill=X)
        label=Label(f3,fg="blue",bg="yellow",font="arial 20 bold")
        label.pack(fill=X)
        update_clock()
        root1.after(15000,return_to_root)
                                                                                    
        root1.mainloop()


if __name__=="__main__":
    #First Window
    root=Tk()
    root.geometry("1280x800")
    root.minsize(1280,800)
    root.maxsize(1280,800)
    root.configure(bg="lavender")
    root.wm_iconbitmap(r"assets\atmicon.ico")
    root.title("ATM MACHINE")
    
    def update_clock():
        current_time = datetime.now().strftime("Date: %Y-%m-%d & Time: %H:%M:%S")
        label.config(text=current_time)
        label.after(1000, update_clock)  # Update every 1000 milliseconds (1 second)


    f=Frame(root,bg="red")
    f.pack(side="top",fill=X)
    l=Label(f,text="WELCOME TO THE ATM",bg="red",fg="white",font="arial 28 bold")
    l.pack(anchor="center")
    f1=Frame(root,bg="lavender")
    f1.pack(side="top",fill=X,pady=60)
    b1=Button(f1,text="Click Here",relief="raised",bg="light green",font="arial 20 bold",command=Create_account)
    b1.pack(side="right",padx=10,pady=20)
    l1=Label(f1,text="Don't Have Account?-Create An Account->",font="arial 20 bold",bg="lavender",padx=15)
    l1.pack(side="right")
    f2=Frame(root,bg="lavender")
    f2.pack(side="top",fill=X,pady=46)
    b2=Button(f2,text="Click Here",relief="raised",bg="light green",font="arial 20 bold",command=get_account)
    b2.pack(side="right",padx=10,pady=20)
    l2=Label(f2,text="Already Have Account?-Cardless Transaction->",font="arial 20 bold",bg="lavender",padx=15)
    l2.pack(side="right")
    f3=Frame(root,bg="lavender")
    f3.pack(side="top",fill=X,pady=60)
    b3=Button(f3,text="Click Here",relief="raised",bg="light green",font="arial 20 bold",command=end)
    b3.pack(side="right",padx=10,pady=30)
    l3=Label(f3,text="EXIT->",font="arial 20 bold",bg="lavender",padx=15)
    l3.pack(side="right")
    f4=Frame(root,bg="yellow")
    f4.pack(fill=X)
    x=datetime.now()
    label=Label(f4,bg="yellow",font="arial 20 bold",fg="blue")
    label.pack(fill=X)
    update_clock()
    root.mainloop()