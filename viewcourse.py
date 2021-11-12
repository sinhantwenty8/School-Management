from tkinter import *
import sqlite3
import editcourseoffer as x

def viewcourse():
    root = Tk()
    root.title("View Course Offering")
    root.geometry("515x620")
    root.configure(background="#ffffcc")

    conn =  sqlite3.connect("studentdetail.sqlite")
    cursor = conn.cursor()
    index=0
    courseList=[]
    def courseOffering ():
        cursor.execute("SELECT * FROM courseOffering")
        index=1
        for _id,coursename,student,date,credittransferable, in cursor:
            if coursename in courseList:
                pass
            else:
                courseList.append(str(coursename))
                coursename_listbox.insert(END,str(index) + " ) " + str(coursename))
                index +=1

    def select():
        anchors = coursename_listbox.get(ANCHOR)
        coursename = anchors[4:]
        shortCourse()

    def shortCourse():
        def dateOfShortCourse():
                anchors = coursename_listbox.get(ANCHOR)
                coursename = anchors[4:]
                date_listbox.delete("0")
                select=("SELECT date FROM courseOffering WHERE coursename = ?")
                cursor.execute(select,(coursename,))
                date=[]
                for d in cursor:
                        date.append(d)
                date_listbox.insert("0",date)
                return

        def studentInCourse():
                anchors = coursename_listbox.get(ANCHOR)
                coursename = anchors[4:]
                studentname_listbox.delete(0,END)
                select=("SELECT name FROM enrolcourse WHERE coursename like ? ")
                cursor.execute(select,(coursename,))
                student=[]
                index=1
                for name, in cursor:
                        student.append(name)
                for s in student:
                    studentname_listbox.insert(END,str(index) + " ) " + str(s))
                    index+=1
                return

        def creditTransferable():
                anchors = coursename_listbox.get(ANCHOR)
                coursename = anchors[4:]
                credit_listbox.delete("0")
                select=("SELECT credittransferable FROM courseOffering WHERE coursename = ?")
                cursor.execute(select,(coursename,))
                credit=[]
                for credittransferable in cursor:
                        credit.append(credittransferable)
                credit_listbox.insert("0",credit)
                return
        dateOfShortCourse()
        creditTransferable()
        studentInCourse()
                
        
    title_label = Label(root, relief = "sunken", text = "-"*20 + "VIEW COURSE OFFERING" + "-"*20,font=("Times",15),bg="#ffcc66",fg="white")
    title_label.grid(columnspan=2,pady=(20))
    frame = Frame(root,bg="#ffcc66")
    frame.grid(row=1,column=0)
    coursename_label = Label(frame , text = "Short Course :",bg="#ffcc66",fg="white",font=("Times",12),justify="left")
    coursename_label.grid(row=1, column=0, sticky=NW, pady=(20,5),padx=10)
    coursename_listbox = Listbox(frame,width=35,height=15)
    coursename_listbox.grid(row=2, column=0,columnspan=2, sticky=W, pady=10,padx=10)

    frame2 = Frame(root,bg="#ffcc66")
    frame2.grid(row=1,column=1)
    student_label = Label(frame2, text = "Student In Course :",bg="#ffcc66",fg="white", font=("Times",12),justify="left")
    student_label.grid(row=1, column=1, sticky=NW,pady=(20,5),padx=10)
    studentname_listbox = Listbox(frame2,width=35,height=15)
    studentname_listbox.grid(row=2, column=1,columnspan=2, sticky=W, pady=10,padx=10)
    
    frame3 = Frame(root,bg="#ffcc66")
    frame3.grid(row=3,column=0,pady=30)
    date_label = Label(frame3, text = "Date :",bg="#ffcc66",fg="white", font=("Times",12),justify="left")
    date_label.grid(row=3, column=0, sticky=N, pady=10,padx=10)
    date_listbox = Listbox(frame3,width=35,height=2)
    date_listbox.grid(row=4, column=0,columnspan=2, sticky=W, pady=10,padx=10)
    
    frame4 = Frame(root,bg="#ffcc66")
    frame4.grid(row=3,column=1,pady=30)
    credittransferable_label = Label(frame4, text = "Credit Transferable :",bg="#ffcc66",fg="white",bd=2, font=("Times",12),justify="left")
    credittransferable_label.grid(row=3, column=1, sticky=N, pady=10,padx=10)
    credit_listbox = Listbox(frame4,width=35,height=2)
    credit_listbox.grid(row=4, column=1,columnspan=2, sticky=W, pady=10,padx=10)

    search_btn = Button(root,width=6, bg="#ffcc66",fg="white", text="Select", font=("Times",12), command = select)
    search_btn.grid(row=5, column=0, columnspan=1, pady=10,padx=40,sticky = "E")
    edit_btn = Button(root,width=5, bg="#ffcc66",fg="white", text="Edit", font=("Times",12), command = x.editcourse)
    edit_btn.grid(row=5, column=1, columnspan=1, pady=10,padx=40,sticky = "W")
    
   
    courseOffering()


    

