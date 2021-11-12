from tkinter import *
import sqlite3
from tkinter import messagebox

def shortcourse():
    root = Tk()
    root.title("Short Course")
    root.geometry("400x500")
    root.configure(background="mistyrose")

    def main():
        db =  sqlite3.connect("studentdetail.sqlite")
        db.execute("CREATE TABLE IF NOT EXISTS shortcourse(coursename TEXT,lecturename TEXT,coursefee INTEGER DEFAULT 0,duration TEXT DEFAULT 0)")
        cursor = db.cursor()
        global courseList
        courseList = []
        cursor.execute("SELECT coursename FROM shortcourse")
        for courseName, in cursor:
            if courseName in courseList:
                pass
            else:
                courseList.append(str(courseName))
        cursor.connection.commit()
        cursor.close()

    def popUpAdd():
        response = messagebox.askyesno("Confirmation","Confirm to add?")
        if response == 1:
            add()
            coursename.delete("0",END)
            lecturename.delete("0",END)
            coursefee.delete("0",END)
            duration.delete("0",END)
        elif response == 0:
            coursename.delete("0",END)
            lecturename.delete("0",END)
            coursefee.delete("0",END)
            duration.delete("0",END)

    def popUpDelete():
        response = messagebox.askyesno("Confirmation","Confirm to delete?")
        if response == 1:
            delete()
            dcoursename.delete("0",END)
        elif response == 0:
            dcoursename.delete("0",END)

    def popUpEdit():
            response = messagebox.askyesno("Confirmation","Confirm to edit?")
            if response == 1:
                edit()
                coursename.delete("0",END)
                lecturename.delete("0",END)
                coursefee.delete("0",END)
                duration.delete("0",END)
            elif response == 0:
                coursename.delete("0",END)
                lecturename.delete("0",END)
                coursefee.delete("0",END)
                duration.delete("0",END)

    def add():
        coursenames = coursename.get()
        lecturenames = lecturename.get()
        coursefees = coursefee.get()
        durations = duration.get()
        main()
        db =  sqlite3.connect("studentdetail.sqlite")
        cursor = db.cursor()
        if coursenames not in courseList and coursenames != "":
            x=("INSERT INTO shortcourse(coursename,lecturename,coursefee,duration)VALUES(?,?,?,?)")
            db.execute(x,(coursenames,lecturenames,coursefees,durations,))
            cursor.connection.commit()
            courseList.append(coursenames)
            response = messagebox.showinfo("Success","Please refresh the short course page to see the updates.")
        else:
            response = messagebox.showerror("Error","Short course is exist or course's name is empty! Course is not added.")

    def delete():
        coursenames = dcoursename.get()
        main()
        db =  sqlite3.connect("studentdetail.sqlite")
        cursor = db.cursor()
        if coursenames in courseList and coursenames != "":
            delete_stu = "DELETE FROM shortcourse WHERE coursename =?"
            cursor.execute(delete_stu,(coursenames,))
            delets = "DELETE FROM courseOffering WHERE coursename =?"
            cursor.execute(delets,(coursenames,))
            delete_stu = "DELETE FROM enrolcourse WHERE coursename =?"
            cursor.execute(delete_stu,(coursenames,))
            cursor.connection.commit()
            cursor.close()
            response = messagebox.showinfo("Success","Please refresh the short course page to see the updates.")
        else:
            response = messagebox.showerror("Error","Course is not exist")

    def edit():
        coursenames = coursename.get()
        lecturenames = lecturename.get()
        coursefees = coursefee.get()
        durations = duration.get()
        main()
        db =  sqlite3.connect("studentdetail.sqlite")
        cursor = db.cursor()
        if coursenames in courseList:
            cursor.execute("UPDATE shortcourse SET lecturename = '{}' WHERE coursename like '{}'".format(lecturenames,coursenames))
            cursor.execute("UPDATE shortcourse SET coursefee = '{}' WHERE coursename like '{}'".format(coursefees,coursenames))
            cursor.execute("UPDATE shortcourse SET duration = '{}' WHERE coursename like '{}'".format(durations,coursenames))
            cursor.connection.commit()
            cursor.close()
            response = messagebox.showinfo("Success","Please refresh the short course page to see the updates.")
        else:
            response = messagebox.showerror("Error","Short course not exist.Course is not updated.")
            
    coursename = Entry(root, width =30, background = "Lavender")
    coursename.grid(row=1, column=1, padx=20, pady=15, sticky=W)
    lecturename = Entry(root, width =30, background = "Lavender")
    lecturename.grid(row=2, column=1, padx=20, pady=15, sticky=W)
    coursefee = Entry(root, width =30, background = "Lavender")
    coursefee.grid(row=3, column=1, padx=20, pady=15, sticky=W)
    duration = Entry(root, width =30, background = "Lavender")
    duration.grid(row=4, column=1, padx=20, pady=15, sticky=W)
    title_label = Label(root, text = "-"*17 + "ADD / EDIT SHORT COURSE " + "-"*18, font=("Times",12), bg="indianred",fg="white")
    title_label.grid(row=0 , column=0, columnspan=2,pady=20)
    coursename_label = Label(root , text = "Short Course :", font=("Times",12), bg="indianred",fg="white")
    coursename_label.grid(row=1, column=0, sticky=E)
    lecturename_label = Label(root, text = "Lecture Name :", font=("Times",12), bg="indianred",fg="white")
    lecturename_label.grid(row=2, column=0, sticky=E)
    coursefee_label = Label(root, text = "Course Fee :", font=("Times",12), bg="indianred",fg="white")
    coursefee_label.grid(row=3, column=0, sticky=E)
    duration_label = Label(root, text = "Duration :", font=("Times",12), bg="indianred",fg="white")
    duration_label.grid(row=4, column=0, sticky=E)
    title_label_delete = Label(root, text = "-"*20 + "DELETE SHORT COURSE" + "-"*20, font=("Times",12), bg="indianred",fg="white")
    title_label_delete.grid(row=6 , column=0, columnspan=2,pady=30)
    dcoursename = Entry(root, width =30, background = "Lavender")
    dcoursename.grid(row=8, column=1, padx=20, pady=10, sticky=W)
    dcoursename_label = Label(root , text = "Short Course :", font=("Times",12), bg="indianred",fg="white")
    dcoursename_label.grid(row=8, column=0, sticky=E)

    edit_btn = Button(root, text="Edit", bg="indianred",fg="white",width=6,command=popUpEdit)
    edit_btn.grid(row=5, column=1, columnspan=1, pady=15,padx=(0,70),sticky=E)
    add_btn = Button(root, text="Add", bg="indianred",fg="white",width=6,command=popUpAdd)
    add_btn.grid(row=5, column=1, columnspan=1, pady=15,padx=20,sticky=W)
    delete_btn = Button(root,text="Delete", bg="indianred",fg="white",command=popUpDelete)
    delete_btn.grid(row=9, column=1, columnspan=2, pady=10,sticky=E,padx=(0,130))
            

