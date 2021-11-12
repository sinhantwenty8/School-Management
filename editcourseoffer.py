from tkinter import *
import sqlite3
from tkinter import messagebox

def editcourse():
    root = Tk()
    root.title("Edit Course Offering")
    root.geometry("440x650")
    root.configure(background="Honeydew")
    

    def courseOffering ():
            global courseList
            courseList=[]
            global courseList2
            courseList2= []
            db =  sqlite3.connect("studentdetail.sqlite")
            db.execute("CREATE TABLE IF NOT EXISTS courseOffering(_id INTEGER PRIMARY KEY AUTOINCREMENT,coursename TEXT,student_id INTEGER DEFAULT 0,date TEXT DEFAULT CURRENT_TIMESTAMP,credittransferable INTEGER DEFAULT 0)")
            cursor = db.cursor()
            cursor.execute("SELECT * FROM courseOffering")
            index=0
            for _id,coursename,student,date,credittransferable, in cursor:
                if coursename in courseList:
                    pass
                else:
                    courseList.append(str(coursename))
                    index +=1
            cursor.execute("SELECT coursename FROM shortcourse")
            for cn, in cursor:
                if cn in courseList:
                    pass
                else:
                    courseList2.append(str(cn))
            cursor.close()
    
    def popUpEdit():
            response = messagebox.askyesno("Confirmation","Confirm to update?")
            if response == 1:
                update()
                credit.delete("0",END)
                cname.delete("0",END)
                date.delete("0",END)
            elif response == 0:
                cname.delete("0",END)
                date.delete("0",END)
                credit.delete("0",END)

    def popUpDelete():
        response = messagebox.askyesno("Confirmation","Confirm to delete?")
        if response == 1:
            delete()
            zname.delete("0",END)
        elif response == 0:
            zname.delete("0",END)

    def popUpAdd():
        response = messagebox.askyesno("Confirmation","Confirm to add?")
        if response == 1:
            add()
            cname.delete("0",END)
            date.delete("0",END)
            credit.delete("0",END)
        elif response == 0:
            cname.delete("0",END)
            date.delete("0",END)
            credit.delete("0",END)

    def update():
        courseOffering ()
        courseName = cname.get()
        def addDate(courseName):
            db =  sqlite3.connect("studentdetail.sqlite")
            cursor = db.cursor()
            user_input = date.get()
            if user_input != "" and courseName != "" and courseName in courseList:
                cursor.execute("UPDATE courseOffering SET date = '{}' WHERE coursename like '{}'".format(user_input,courseName))
                cursor.connection.commit()
                response = messagebox.showinfo("Success","Please refresh the course offering page to see the updates.")
            else:
                response = messagebox.showerror("Error","Course not exist or Course's date is empty!Course's date is not updated.")
    

        def addCreditTransferable(courseName):
            courseOffering ()
            db =  sqlite3.connect("studentdetail.sqlite")
            cursor = db.cursor()
            user_input = credit.get()
            if user_input != "" and courseName != "" and courseName in courseList:
                if user_input.isdigit()==True:
                    cursor.execute("UPDATE courseOffering SET credittransferable = '{}' WHERE coursename like '{}'".format(user_input,courseName))
                else:
                    response = messagebox.showerror("Error","Input must be digit! Credits Transferable is not updated.")
            else:
                response = messagebox.showerror("Error","Course not exist or Credits transferable is empty!Credits transferable is not updated.")
            cursor.connection.commit()
            
        addDate(courseName)
        addCreditTransferable(courseName)

    def add():
        courseOffering ()
        db =  sqlite3.connect("studentdetail.sqlite")
        cursor = db.cursor()
        courseName = cname.get()
        creditTransferable = credit.get()
        dates = date.get()
        if courseName not in courseList and courseName != "" and courseName in courseList2:
            x = ("INSERT INTO courseOffering (coursename, date,credittransferable) VALUES (?,?,?)")
            db.execute(x,(courseName,dates,creditTransferable))
            cursor.connection.commit()
            courseList.append(courseName)
            response = messagebox.showinfo("Success","Please refresh the course offering page to see the updates.")

        else:
            response = messagebox.showerror("Error","Course is exist or course's name is empty! Course is not added.")
        

    def delete():
        db =  sqlite3.connect("studentdetail.sqlite")
        cursor = db.cursor()
        courseName = zname.get()
        if courseName in courseList and courseName != "":
            delete_stu = "DELETE FROM enrolcourse WHERE coursename =?"
            cursor.execute(delete_stu,(courseName,))
            delets = "DELETE FROM courseOffering WHERE coursename =?"
            cursor.execute(delets,(courseName,))
            cursor.connection.commit()
            cursor.close()
            response = messagebox.showinfo("Success","Please refresh the course offering page to see the updates.")
        else:
            response = messagebox.showerror("Error","Course is not exist")
        

    title_label = Label(root, relief = "sunken", text = "-"*16 + "EDIT COURSE OFFERING " + "-"*17,font=("Times",15),bg="darkseagreen",fg="white")
    title_label.grid(columnspan=2,pady=15)
    coursename_label = Label(root,justify="center" , text = "Short Course :",bg="darkseagreen",fg="white",font=("Times",11))
    coursename_label.grid(row=1, column=0,columnspan=2, pady=15)
    cname = Entry(root,justify="center", width =40, background = "Lavender")
    cname.grid(row=2, column=0,columnspan=2, pady=15)
    date_label = Label(root , text = "Course's Date :",bg="darkseagreen",fg="white",font=("Times",11),justify="left")
    date_label.grid(row=3, column=0,columnspan=2, pady=(20,5),padx=15)
    date = Entry(root,justify="center", width =40, background = "Lavender")
    date.grid(row=4, column=0,columnspan=2, pady=15)
    credit_label = Label(root ,justify="center", text = "Credits Transferable :",bg="darkseagreen",fg="white",font=("Times",11))
    credit_label.grid(row=5, column=0,columnspan=2, pady=15)
    credit = Entry(root, width =40, background = "Lavender",justify="center")
    credit.grid(row=6, column=0,columnspan=2, pady=15)
    titles_label = Label(root, relief = "sunken", text = "-"*15 + "DELETE COURSE OFFERING" + "-"*14,font=("Times",15),bg="darkseagreen",fg="white")
    titles_label.grid(row=8,columnspan=2,pady=15)

    edit_btn = Button(root, bg="Darkseagreen",fg="white", text="Add Course",command=popUpAdd)
    edit_btn.grid(row=7, column=0, pady=20, sticky=W, padx=90)
    edit_btn = Button(root, bg="Darkseagreen",fg="white", text="Edit Course",justify="left",command=popUpEdit)
    edit_btn.grid(row=7, column=1, pady=20, sticky=W,padx=(0,100))
    edit_btn = Button(root, bg="Darkseagreen",fg="white", text="Delete Course",justify="center",command=popUpDelete)
    edit_btn.grid(row=11, columnspan=2, pady=20, padx=(0,195),sticky="E")

    coursenames_label = Label(root,justify="center" , text = "Short Course :",bg="darkseagreen",fg="white",font=("Times",11))
    coursenames_label.grid(row=9, column=0,columnspan=2, pady=15)
    zname = Entry(root,justify="center", width =40, background = "Lavender")
    zname.grid(row=10, column=0,columnspan=2, pady=15)
    
    
    courseOffering ()


    

    


