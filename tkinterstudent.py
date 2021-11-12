from tkinter import *
import sqlite3
from tkinter import messagebox
import viewstudentname as x

def student():
    root = Tk()
    root.title("Student")
    root.geometry("400x550")
    root.configure(background="LightSteelBlue")
    
    def main():
        global nameList
        global emailList
        conn =  sqlite3.connect("studentdetail.sqlite")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS student(_id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,email TEXT,gender INTEGER,coursename TEXT)")
        emailList = []
        nameList = []
        cursor.execute("SELECT * FROM student")
        index=0
        for _id,name,email,gender,coursename in cursor:
            if email in emailList:
                pass
            else:
                emailList.append(str(email))
                index +=1
            if name in nameList:
                pass
            else:
                nameList.append(str(name))
        cursor.connection.commit()
        cursor.close()

    def submit():
        main()
        print(nameList)
        studentName = name.get()
        student_email = email.get()
        if studentName not in nameList:
            conn =  sqlite3.connect("studentdetail.sqlite")
            cursor = conn.cursor()
            nameList.append(studentName)
            if gender.get() == "male":
                gen = 0
                if student_email in emailList:
                    print("Email already exist.Please use another email.")
                    response = messagebox.showwarning("Error","Email exist! Student is not added.")
                else:
                    cursor.execute("INSERT INTO student (name,email,gender) VALUES  (:name, :email, :gender)",{'name' : name.get(), 'email' : email.get(), 'gender' : gen})
                    print("Successful")
                    emailList.append(email)
            elif gender.get() == "female":
                gen = 1
                if student_email in emailList:
                    print("Email already exist.Please use another email.")
                    response = messagebox.showwarning("Error","Email exist! Student is not added.")
                else:
                    cursor.execute("INSERT INTO student (name,email,gender) VALUES  (:name, :email, :gender)",{'name' : name.get(), 'email' : email.get(), 'gender' : gen})
                    print("Successful")
                    emailList.append(email)
            else:
                response = messagebox.showwarning("Error","Gender input incorrect.Student not added.Please enter male or female.")
                cursor.connection.commit()
                
            cursor.connection.commit()
            cursor.close()
        else:
            response = messagebox.showwarning("Error","Student exist.")
            

    def delete():
        main()
        if student in nameList:
            conn =  sqlite3.connect("studentdetail.sqlite")
            cursor = conn.cursor()
            studentName=sname.get()
            delete_sql = "DELETE FROM student WHERE name = ?"
            cursor.execute(delete_sql,(studentName,))
            delete_stu = "DELETE FROM enrolcourse WHERE name =?"
            cursor.execute(delete_stu,(studentName,))
            nameList.remove(studentName)
            cursor.connection.commit()
            cursor.close()
        
        else:
            response = messagebox.showwarning("Error","Student not exist.")
            

    def edit():
        main()
        conn =  sqlite3.connect("studentdetail.sqlite")
        cursor = conn.cursor()
        studentName= ename.get()
        email= eemail.get()
        gender= egender.get()
        if email in emailList:
            print("Email already exist.Please use another email.")
            response = messagebox.showwarning("Error","Email exist! Email is not updated.")
        else:
            cursor.execute("UPDATE student SET email = '{}' WHERE name = '{}'".format(email,studentName))
            print("Successful")
            cursor.connection.commit()
            emailList.append(email)
        if gender == "male":
            gen = 0
            cursor.execute("UPDATE student SET gender = '{}' WHERE name = '{}'".format(gen,studentName))
        elif gender == "female":
            gen = 1
            cursor.execute("UPDATE student SET gender = '{}' WHERE name = '{}'".format(gen,studentName))
        else:
            print("INVALID INPUT")
            response = messagebox.showwarning("Invalid","Invalid input for gender! Gender is not updated.")
            
        cursor.connection.commit()
        cursor.close()
            
    def popUpAdd():
        response = messagebox.askyesno("Confirmation","Confirm to add?")
        if response == 1:
            submit()
            name.delete("0",END)
            email.delete("0",END)
            gender.delete("0",END)
        elif response == 0:
            name.delete("0",END)
            email.delete("0",END)
            gender.delete("0",END)

    def popUpDelete():
        response = messagebox.askyesno("Confirmation","Confirm to delete?")
        if response == 1:
            delete()
            sname.delete("0",END)
        elif response == 0:
            sname.delete("0",END)

    def popUpEdit():
            response = messagebox.askyesno("Confirmation","Confirm to edit?")
            if response == 1:
                edit()
            elif response == 0:
                ename.delete("0",END)
                eemail.delete("0",END)
                egender.delete("0",END)

    name = Entry(root, width =30, background = "Lavender")
    name.grid(row=1, column=1, padx=20, pady=10, sticky=W)
    email = Entry(root, width =30, background = "Lavender")
    email.grid(row=2, column=1, padx=20, pady=10, sticky=W)
    gender = Entry(root, width =30, background = "Lavender")
    gender.grid(row=3, column=1, padx=20, pady=10, sticky=W)
    sname = Entry(root, width =30, background = "Lavender")
    sname.grid(row=7, column=1, padx=20, pady=10, sticky=W)
    ename = Entry(root, width =30, background = "Lavender")
    ename.grid(row=10, column=1, padx=20, pady=10, sticky=W)
    eemail = Entry(root, width =30, background = "Lavender")
    eemail.grid(row=11, column=1, padx=20, pady=10, sticky=W)
    egender = Entry(root, width =30, background = "Lavender")
    egender.grid(row=12, column=1, padx=20, pady=10, sticky=W)

    title_label = Label(root, text = "-"*32 + "ADD STUDENT" + "-"*32,)
    title_label.grid(row=0 , column=0, columnspan=2,pady=10)
    name_label = Label(root , text = "Name :")
    name_label.grid(row=1, column=0, sticky=E)
    email_label = Label(root, text = "Email :")
    email_label.grid(row=2, column=0, sticky=E)
    gender_label = Label(root, text = "Gender :")
    gender_label.grid(row=3, column=0, sticky=E)
    title_label_delete = Label(root, text = "-"*31 + "DELETE STUDENT" + "-"*31)
    title_label_delete.grid(row=6 , column=0, columnspan=2,pady=15)
    sname_label = Label(root , text = "Name :")
    sname_label.grid(row=7, column=0, sticky=E)
    title_label_edit = Label(root, text = "-"*29 + "EDIT STUDENT'S INFO" + "-"*28)
    title_label_edit.grid(row=9 , column=0, columnspan=2,pady=10)
    ename_label = Label(root , text = "Name :")
    ename_label.grid(row=10, column=0, sticky=E)
    eemail_label = Label(root, text = "Email :")
    eemail_label.grid(row=11, column=0, sticky=E)
    egender_label = Label(root, text = "Gender :")
    egender_label.grid(row=12, column=0, sticky=E)

    submit_btn = Button(root, bg="RoyalBlue",fg="white", text="Add Record", command = popUpAdd)
    submit_btn.grid(row=4, column=0, columnspan=2, pady=10)
    delete_btn = Button(root, bg="RoyalBlue",fg="white", text="Delete Record", command = popUpDelete)
    delete_btn.grid(row=8, column=0, columnspan=2, pady=10)
    edit_btn = Button(root, bg="RoyalBlue",fg="white", text="Edit Record", command = popUpEdit)
    edit_btn.grid(row=13, column=0, columnspan=2, pady=10)
    student_btn = Button(root, bg="RoyalBlue",fg="white", text="Student", command = x.viewStudentName)
    student_btn.grid(row=13, column=0, columnspan=2, pady=10,sticky=W,padx=30)
    
    main()



