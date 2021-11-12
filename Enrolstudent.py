from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3

def enrolStudent():
    root = Tk()
    root.title("Student Enrolment")
    root.geometry("400x550")
    root.configure(background="Wheat")
    global nameList
    global courseList
    courseList = []
    nameList = []

    def main():
        conn =  sqlite3.connect("studentdetail.sqlite")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS enrolcourse(name TEXT,coursename TEXT)")
        cursor.execute("SELECT * FROM student")
        for _id,name,email,gender,coursename in cursor:
            if name in nameList:
                pass
            else:
                nameList.append(str(name))
                
        cursor.execute("SELECT * FROM courseOffering")
        index=1
        for _id,coursename,student,date,credittransferable, in cursor:
            if coursename in courseList:
                pass
            else:
                courseList.append(str(coursename))
                coursename_listbox.insert(END,str(index) + " ) " + str(coursename))
                index +=1
                


    def popUpEdit():
        response = messagebox.askyesno("Confirmation","Confirm to enrol student?")
        if response == 1:
            enrolStudent()
            name.delete("0",END)
        elif response == 0:
            name.delete("0",END)

    def popUpDelete():
        response = messagebox.askyesno("Confirmation","Confirm to de-enrol student?")
        if response == 1:
            deenrolStudent()
            name.delete("0",END)
        elif response == 0:
            name.delete("0",END)

    def enrolStudent():
        main()
        student = name.get()
        anchors = coursename_listbox.get(ANCHOR)
        coursename = anchors[4:]
        conn =  sqlite3.connect("studentdetail.sqlite")
        cursor = conn.cursor()
        if coursename != "":
            if student in nameList:
                select=("INSERT INTO enrolcourse VALUES (?,?)")
                cursor.execute(select,(student,coursename))
                cursor.connection.commit()
            else:
                response = messagebox.showerror("Error","Student not exist")
        else:
            response = messagebox.showerror("Error","Course is not selected")
            
    def deenrolStudent():
        main()
        anchors = coursename_listbox.get(ANCHOR)
        coursename = anchors[4:]
        student = name.get()
        conn =  sqlite3.connect("studentdetail.sqlite")
        cursor = conn.cursor()
        if coursename != "":
            if student in nameList:
                select=("DELETE FROM enrolcourse WHERE name = ? and coursename = ?")
                cursor.execute(select,(student,coursename))
                cursor.connection.commit()
            else:
                response = messagebox.showerror("Error","Student not exist")
        else:
            response = messagebox.showerror("Error","Course is not selected")
       
                 
    title_label = Label(root, relief = "sunken", bg="Tan",font=("Times",15),fg="white",text = "-"*10 + "ENROL/DE-ENROL STUDENT" + "-"*10,)
    title_label.grid(row=0 , column=0, columnspan=2,pady=10)
    name_label = Label(root ,font=("Times",12), text = "Name :", bg="Tan",fg="white")
    name_label.grid(row=3, column=0,sticky=W,padx=10,pady=(30,0))
    name = Entry(root, width =30, background = "Lavender",bg="ivory")
    name.grid(row=4, column=0, padx=10, pady=10, sticky=W)
    coursename_label = Label(root , bg="Tan",font=("Times",12), text = "Short Course :",fg="white",justify="left")
    coursename_label.grid(row=1, column=0, sticky=NW, pady=(20,5),padx=10)
    coursename_listbox = Listbox(root,width=35,height=15,bg="ivory")
    coursename_listbox.grid(row=2, column=0,columnspan=2, sticky=W, pady=10,padx=10)
    deenrol_btn = Button(root,bg="Tan",fg="white", text="De-enrol", command = popUpDelete)
    deenrol_btn.grid(row=5, column=0,pady=10,padx=90)
    enrol_btn = Button(root,bg="Tan",fg="white", width=6,text="Enrol",command=popUpEdit)
    enrol_btn.grid(row=5, column=0, pady=10,sticky="W",padx=10)

    main()         

    
        
        
                       
