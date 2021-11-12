from tkinter import *
import sqlite3
import shortcourseGUI as y

def viewshortcourse():
    root = Tk()
    root.title("View Short Course")
    root.geometry("515x620")
    root.configure(background="lightpink")
    conn =  sqlite3.connect("studentdetail.sqlite")
    cursor = conn.cursor()
    index=0
    courseList=[]
    
    def main():
        cursor.execute("SELECT coursename FROM shortcourse")
        index=1
        for cn, in cursor:
            if cn in courseList:
                pass
            else:
                courseList.append(str(cn))
                coursename_listbox.insert(END,str(index) + " ) " + str(cn))
                index +=1
                
    def select():
        anchors = coursename_listbox.get(ANCHOR)
        coursename = anchors[4:]
        show()

    def show():
        anchors = coursename_listbox.get(ANCHOR)
        coursename = anchors[4:]
        
        def lecturers():
            lecturer_listbox.delete("0",END)
            select=("SELECT lecturename FROM shortcourse WHERE coursename = ?")
            cursor.execute(select,(coursename,))
            lecturers = []
            for l in cursor:
                lecturers.append(l)
            lecturer_listbox.insert("0",lecturers)

        def coursefee():
            coursefee_listbox.delete("0",END)
            select=("SELECT coursefee FROM shortcourse WHERE coursename = ?")
            cursor.execute(select,(coursename,))
            fee = []
            for l in cursor:
                fee.append(l)
            coursefee_listbox.insert("0",fee)

        def duration():
            duration_listbox.delete("0",END)
            select=("SELECT duration FROM shortcourse WHERE coursename = ?")
            cursor.execute(select,(coursename,))
            durations = []
            for l in cursor:
                durations.append(l)
            duration_listbox.insert("0",durations)

        lecturers()
        coursefee()
        duration()
                        

    title_label = Label(root, relief = "sunken", text = "-"*24 + "VIEW SHORT COURSE" + "-"*21,font=("Times",15),bg="hotpink",fg="white")
    title_label.grid(columnspan=2,pady=(20))
    frame = Frame(root,bg="hotpink")
    frame.grid(row=1,column=0)
    coursename_label = Label(frame , text = "Short Course :",bg="pink",fg="white",font=("Times",12),justify="left")
    coursename_label.grid(row=1, column=0, sticky=NW, pady=(20,5),padx=10)
    coursename_listbox = Listbox(frame,width=35,height=15)
    coursename_listbox.grid(row=2, column=0,columnspan=2, sticky=W, pady=10,padx=10)

    frame2 = Frame(root,bg="hotpink")
    frame2.grid(row=1,column=1)
    lecturer_label = Label(frame2, text = "Course's Lecturer :",bg="pink",fg="white", font=("Times",12),justify="left")
    lecturer_label.grid(row=1, column=1, sticky=NW,pady=(20,5),padx=10)
    lecturer_listbox = Listbox(frame2,width=35,height=15)
    lecturer_listbox.grid(row=2, column=1,columnspan=2, sticky=W, pady=10,padx=10)
    
    frame3 = Frame(root,bg="hotpink")
    frame3.grid(row=3,column=0,pady=30)
    coursefee= Label(frame3, text = "Course's Fee :",bg="pink",fg="white", font=("Times",12),justify="left")
    coursefee.grid(row=3, column=0, sticky=N, pady=10,padx=10)
    coursefee_listbox = Listbox(frame3,width=35,height=2)
    coursefee_listbox.grid(row=4, column=0,columnspan=2, sticky=W, pady=10,padx=10)
    
    frame4 = Frame(root,bg="hotpink")
    frame4.grid(row=3,column=1,pady=30)
    duration_label = Label(frame4, text = "Course's Duration :",bg="pink",fg="white",bd=2, font=("Times",12),justify="left")
    duration_label.grid(row=3, column=1, sticky=N, pady=10,padx=10)
    duration_listbox = Listbox(frame4,width=35,height=2)
    duration_listbox.grid(row=4, column=1,columnspan=2, sticky=W, pady=10,padx=10)

    search_btn = Button(root,width=6, bg="hotpink",fg="white", text="Select", font=("Times",12),command=select)
    search_btn.grid(row=5, column=0, columnspan=1, pady=10,padx=40,sticky = "E")
    edit_btn = Button(root,width=5, bg="hotpink",fg="white", text="Edit", font=("Times",12),command=y.shortcourse)
    edit_btn.grid(row=5, column=1, columnspan=1, pady=10,padx=40,sticky = "W")

    
    main()
 

