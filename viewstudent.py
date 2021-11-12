from tkinter import *
import sqlite3
import Enrolstudent as enrol

def viewStudent():
    root = Tk()
    root.title("View Student")
    root.geometry("500x500")
    root.configure(background="LavenderBlush")
    
    def email(studentName):
        conn =  sqlite3.connect("studentdetail.sqlite")
        cursor = conn.cursor()
        emails=[]
        email_listbox.delete(0)
        cursor.execute("SELECT email FROM student where name = '{}'".format(studentName))
        for i, in cursor:
            emails.append(i)
        email_listbox.insert(END,emails)

    def gender(studentName):
        global a
        conn =  sqlite3.connect("studentdetail.sqlite")
        cursor = conn.cursor()
        genders=[]
        gender_listbox.delete(0)
        cursor.execute("SELECT gender FROM student where name = '{}'".format(studentName))
        for i, in cursor:
            print(i)
            if i == 1:
                a=1
            else:
                a=0
            gen =["male","female"]
            g=gen[a]
            genders.append(g)
        gender_listbox.insert(END,genders)
        
    def course(studentName):
        conn =  sqlite3.connect("studentdetail.sqlite")
        cursor = conn.cursor()
        course=[]
        index=1
        course_listbox.delete(0,END)
        cursor.execute("SELECT coursename FROM enrolcourse where name = '{}'".format(studentName))
        for i, in cursor:
            if i not in course:
                course.append(i)
        for s in course:
            course_listbox.insert(END,str(index) + ") " + str(s))
            index += 1        

    def searchs(studentName):
        conn =  sqlite3.connect("studentdetail.sqlite")
        cursor = conn.cursor()
        name=[]
        for i, in cursor:
            name.append(i)
        if studentName not in name:
            course_listbox.delete(0,END)
            gender_listbox.delete(0,END)
            email_listbox.delete(0,END)
            email_listbox.insert(0,"-")
            name.insert(0,"-")
        else:
            cursor.execute("SELECT name FROM student where name = '{}'".format(studentName))
        
              
        email(studentName)
        gender(studentName)
        course(studentName)
    

    title_label = Label(root, relief = "sunken", text = "-"*20 + "VIEW STUDENT DETAILS" + "-"*20,font=("Times",15),bg="thistle",fg="white")
    title_label.grid(row=0 , columnspan=3,pady=20)
    name_label = Label(root , text = "Name :",bg="thistle",fg="white",font=("Times",12))
    name_label.grid(row=1, column=0, sticky=NE, pady=20,padx=10)
    email_label = Label(root, text = "Email :",bg="thistle",fg="white", font=("Times",12))
    email_label.grid(row=2, column=0, sticky=NE,pady=20,padx=10)
    gender_label = Label(root, text = "Gender :",bg="thistle",fg="white", font=("Times",12))
    gender_label.grid(row=3, column=0, sticky=NE, pady=20,padx=10)
    course_label = Label(root, text = "Course Enrolled :",bg="thistle",fg="white",bd=2, font=("Times",12))
    course_label.grid(row=4, column=0, sticky=NE, pady=20,padx=10)

    email_listbox = Listbox(root,width=30,height=1)
    email_listbox.grid(row=2, column=1,columnspan=2, sticky=W, pady=20,padx=20)
    gender_listbox = Listbox(root,width=30,height=1)
    gender_listbox.grid(row=3, column=1,columnspan=2, sticky=W, pady=20,padx=20)
    course_listbox = Listbox(root,width=30,height=7)
    course_listbox.grid(row=4, column=1,columnspan=2, sticky=W, pady=20,padx=20)
    name = Entry(root, width =30, background = "white")
    name.grid(row=1, column=1, padx=20, pady=10, sticky=W)

    search_btn = Button(root, bg="thistle",fg="white", text="Search", font=("Times",12), command = lambda :searchs(name.get()))
    search_btn.grid(row=5, column=1, columnspan=2, pady=10,sticky=E,padx=(0,180))
    enrol_btn = Button(root, bg="thistle",fg="white", text="Course enrolment", font=("Times",12), command = enrol.enrolStudent)
    enrol_btn.grid(row=5, column=0, columnspan=2, pady=10,sticky=W,padx=40)
 

    
