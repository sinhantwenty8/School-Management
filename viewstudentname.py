from tkinter import *
import sqlite3
import Enrolstudent as enrol

def viewStudentName():
    root = Tk()
    root.title("View Total Student")
    root.geometry("340x500")
    root.configure(background="LavenderBlush")

    def student():
        conn =  sqlite3.connect("studentdetail.sqlite")
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM student")
        students = []
        for d, in cursor:
            students.append(d)
        
        index = 1
        for student in students:
            name_listbox.insert(END,str(index) + ") "+ student)
            index += 1
        
    

    title_label = Label(root, relief = "sunken", text = "-"*20 + "Student" + "-"*20,font=("Times",15),bg="thistle",fg="white")
    title_label.grid(row=0 , columnspan=3,pady=20)
    name_label = Label(root , text = " Student Name :",bg="thistle",fg="white",font=("Times",12))
    name_label.grid(row=1, column=0, sticky=W, pady=20,padx=10)
    name_listbox = Listbox(root,width=30,height=20)
    name_listbox.grid(row=2, column=0, sticky=W, pady=0,padx=10)

    student()

    


