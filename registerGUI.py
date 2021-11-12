from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

def register():

    top= Tk()
    top.geometry("500x500")
    top.title("Register")
    top.configure(background="Thistle")


    class User:
      def __init__(self, password, username):
        self.password = password
        self.username = username

      def getPassword(self):
        return self.password

      def getUsername(self):
        return (self.username)

    def popUpAdd():
        response = messagebox.askyesno("Confirmation","Register Now?")
        if response == 1:
            registers()
        elif response == 0:
            name.delete("0",END)
            email.delete("0",END)
            gender.delete("0",END)

    def registers():
        if entry2.get() != "" and entry1.get() != "":
            password = entry2.get()
            confirm_pass = centry2.get()
            if password == confirm_pass:
                fileA = open("userData.txt", "a")
                pw = entry2.get()
                un = entry1.get()
                registerInfo = (f'{un},{pw},{"0"} \n')
                fileA.write(registerInfo)
                fileA.close()
                entry1.delete("0",END)
                entry2.delete("0",END)
                centry2.delete("0",END)
                top.destroy()
                
            else:
                response = messagebox.showerror("Error","Password not match.")
        else:
            print("nothing")

    
    register = Label(top,text="Register",font=("Helevtica",17),justify="center",background="mediumpurple",fg="white",relief="sunken")
    register.grid(row=0,column=1,columnspan=2,pady=30,padx=(0,0))
    username = Label(top, text="Username:", font=("Helevtica",12),justify="center",background="mediumpurple",fg="white",relief="sunken")
    username.grid(row=1, column=1, pady=(30,10),padx=215)
    entry1 = Entry(top, width=40,bd=2,justify="center")
    entry1.grid(row=2, column=1, pady=10,)
    password = Label(top, text="Password:", font=("Helevtica",12),background="mediumpurple",fg="white",relief="sunken")
    password.grid(row=3, column=1, pady=10)
    entry2 = Entry(top,width=40,bd=2,show="*",justify="center")
    entry2.grid(row=4, column=1, pady=10,)
    cpassword = Label(top, text="Confirm Password:", font=("Helevtica",12),background="mediumpurple",fg="white",relief="sunken")
    cpassword.grid(row=5, column=1, pady=10)
    centry2 = Entry(top,width=40,bd=2,show="*",justify="center")
    centry2.grid(row=6, column=1, pady=10,)

    register_btn = Button(top, bg="mediumpurple",fg="white", text="Register",font=("Helevtica",8),command=popUpAdd)
    register_btn.grid(row=7, column=1,pady=10)

        

