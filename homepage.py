from tkinter import *
import sqlite3
import tkinterstudent as x
import viewstudent as y
import viewcourse as z
import viewshortcourse as w

def home():
    home = Tk()
    home.title("Home Page")
    home.geometry("830x500")
    home.configure(background = "DarkSalmon")


    title_label = Label(home,font=("Helvetica",30),fg="white",bg = "DarkSalmon",bd=2, relief ="sunken",text = "HOME",justify="center")
    title_label.grid(row=0 , column=0, columnspan=2,pady=30,padx=360)

    student_btn = Button(home,font=("Helvetica",25),width=13,height=2,bg="Salmon",bd=3, fg="white", text="Edit Student", command=x.student) 
    student_btn.grid(row=4, column=0, columnspan=1, pady=30,padx=0)
    course_btn = Button(home,font=("Helvetica",25),width=13,height=2,bg="Salmon",bd=3,  fg="white", text="Course Offering", command=z.viewcourse) 
    course_btn.grid(row=5, column=1, columnspan=1, pady=10,padx=0)
    viewstudent_btn = Button(home,font=("Helvetica",25),width=13,height=2,bg="Salmon",bd=3,  fg="white", text="View Student", command=y.viewStudent) 
    viewstudent_btn.grid(row=4, column=1, columnspan=1, pady=30,padx=0)
    editcourse_btn = Button(home,font=("Helvetica",25),width=13,height=2,bg="Salmon",bd=3,  fg="white", text="Short Course", command=w.viewshortcourse) 
    editcourse_btn.grid(row=5, column=0, columnspan=1, pady=30,padx=0)


