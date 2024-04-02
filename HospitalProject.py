from tkinter import *
import tkinter as tk
from tkinter.font import Font
from tkinter import messagebox
import pywhatkit

user_data={}
aa=[]
bb=[]
cc=[]
def display_info():
    aaa = display_username.get()
    bbb = display_srno.get()
    s = gender_var.get()
    if bb[0]==cc[0] and cc[1]==1234:
        print("Data found in user_data")
        disease = user_data[aaa]['disease']
        messagebox.showinfo("Information", f"Additional information for {aaa}\nYour serial no is : {bbb}\nYour gender is : {bb[1]}\nYour disease is : {bb[2]}")
    else:
        print("Data not found in user_data or serial number mismatch")
        messagebox.showinfo("Warning", "Enter valid information")


def count():
    aa.append(1)
    b=len(aa)
    if(b>=2):
        messagebox.showwarning("Doctor Selection","Select any one doctor")
def store_data():
    global patientvalue, ageentry, gender_var, diseaseentry
    username = patientvalue.get()
    bb.append(username)
    print(username)
    gender = gender_var.get()
    bb.append(gender)
    print(gender)
    disease = diseaseentry.get()
    bb.append(disease)
    print(disease)
    user_data[username] = {'serial_number': 1234, 'gender': gender, 'disease': disease}  # Store complete form data
    messagebox.showinfo("Approved", f"Form submitted successfully for {username}\nYour s.r number is : 1234")

def done():
        messagebox.showinfo("Doctor Selection","Doctor Selected Successfully")

def subform():
    print("Here is the list of doctors")
    root=Tk()

    root.geometry("600x400")
    #root.minsize(300,400)
    #root.maxsize(300,400)
    title_font=Font(family="Helvetica",size=12,weight="bold")
    root.title("Our doctors list")
    root.option_add("*Font",title_font)
    Label(root,text="Doctors List",font=("Helvetica",15,"bold")).grid(row=0,column=1)
    Label(root,text="^Select the doctor you have to appoint^",font=("Helvetica",10),pady=10).grid(row=1,column=0)
    Label(root,text="Dr. Nikhil Malewar",font=("comicsansms",11,"bold")).grid(row=2,column=0)
    Label(root,text="Dr. Ajaya Nand Jha",font=("comicsansms",11,"bold")).grid(row=3,column=0)
    Label(root,text="Dr. Suresh Joshi",font=("comicsansms",11,"bold")).grid(row=4,column=0)
    Label(root,text="Dr. Abhijit Dey",font=("comicsansms",11,"bold")).grid(row=5,column=0)
    Label(root,text="Dr. Aroop Mukherjee",font=("comicsansms",11,"bold")).grid(row=6,column=0)
    Label(root,text="Dr. B. K R Balakrishnan",font=("comicsansms",11,"bold")).grid(row=7,column=0)
    Label(root,text="Dr. Akshay Batra",font=("comicsansms",11,"bold")).grid(row=8,column=0)
    doc=IntVar()
    Checkbutton(root,text=" :",textvariable=doc,command=count).grid(row=2,column=1)
    Checkbutton(root,text=" :",textvariable=doc,command=count).grid(row=3,column=1)
    Checkbutton(root,text=" :",textvariable=doc,command=count).grid(row=4,column=1)
    Checkbutton(root,text=" :",textvariable=doc,command=count).grid(row=5,column=1)
    Checkbutton(root,text=" :",textvariable=doc,command=count).grid(row=6,column=1)
    Checkbutton(root,text=" :",textvariable=doc,command=count).grid(row=7,column=1)
    Checkbutton(root,text=" :",textvariable=doc,command=count).grid(row=8,column=1)
    Button(root,text="Submit",command=done).grid(row=9)
    root.mainloop()

root=Tk()

print("""Welcome to our Sambhajinagar Hospital\n      Here is our services\n             *""")
print("Enter 1 to fill the form")
print("Enter 2 to see the details")
print("Enter 3 to see who is the doctor")
print("Enter 4 to exit")
print("Enter 5 to rerun the program")

a=int(input())
root.geometry("400x400")
root.maxsize(400,400)
root.title("patient form")
Label(root,text="Patient Form",fg="black",font=("comicsansms",17,"bold"),padx=14,pady=17).grid()
if(a==1):
    b=Label(root,text="Patient Name :",fg="black",pady=7)
    b.grid(row=1,column=0)
    patientvalue=StringVar()
    patiententry=Entry(root,textvariable=patientvalue)
    patiententry.grid(row=1,column=1)
    c=Label(root,text="Patient Age : ",fg="black",pady=5).grid(row=2,column=0)
    patientage=IntVar()
    ageentry=Entry(root,textvariable=patientage).grid(row=2,column=1)
    gender_label = Label(root, text="Gender:").grid(row=3, column=0)
    gender_var = StringVar(value="Male")
    gender_male_radio = tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=3, column=1)
    gender_female_radio = tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=3, column=2)
    e=Label(root,text="Disease : ",fg="black",pady=5).grid(row=4,column=0)
    patientdisease=StringVar()
    diseaseentry=Entry(root,textvariable=patientdisease)
    diseaseentry.grid(row=4,column=1)
    Checkbutton(root,text="Do you want to see list of doctors",command=subform).grid(row=5,column=0)
    Button(root,text="Submit",command=store_data,pady=7).grid(row=6,column=1)
    root.mainloop()
    print("Enter 2 to see the details")
    print("Enter 3 to see who is the doctor")
    print("Enter 4 to exit")
    print("Enter 5 to rerun the program")
    b=int(input())
if(a==2 or b==2):
    print("Enter your details")
    root=Tk()
    root.title("Display Patients Information")
    root.geometry("300x400")
    Label(root,text="Enter registered username").grid(row=0,column=0)
    display_username=StringVar()
    cc.append(display_username)
    display_username_entry=Entry(root,textvariable=display_username).grid(row=0,column=1)
    Label(root,text="Enter your Sr.No").grid(row=1,column=0)
    display_srno=IntVar()
    cc.append(display_srno)
    display_srno_entry=Entry(root,textvariable=display_srno).grid(row=1,column=1)
    Button(root,text="Check",command=display_info()).grid(row=2,column=1)
    root.mainloop()

root.mainloop()
