from tkinter import *
from PIL import ImageTk,Image
import homepage as x
from tkinter import messagebox
import registerGUI as registerGUI


def login():
  top= Tk()
  top.geometry("700x500")
  top.title("Login")
  top.configure(background="white")

  class User:
    def __init__(self, password, username):
      self.password = password
      self.username = username

    def getPassword(self):
      return self.password

    def getUsername(self):
      return (self.username)

  def login():
      userDict = {}
      userList = []

      f = open("userData.txt", 'r')
      countNum = 0

      for line in f.readlines():
          userItem = line.strip()
          valueInterm = userItem.split(',')
          valueUsername = valueInterm[0]
          valuePassword = valueInterm[1]
          valueLock = valueInterm[2]
          userDict[valueUsername] = {
              "name": valueUsername,
              "password": valuePassword,
              "lock": valueLock
              }
          f.close()
          userName = entry1.get()
          
      if str(userName) != "":
         if str(userName) in str(userDict.keys()):
            password = entry2.get()
            if str(password) == userDict[str(userName)]["password"]:
                top.destroy()
                x.home()
            else:
              entry1.delete("0",END)
              entry2.delete("0",END)
              response = messagebox.showwarning("Error","Wrong Password.")
         else:
            entry1.delete("0",END)
            entry2.delete("0",END)
            response = messagebox.showwarning("Error","User not exist.")
      else:
        response = messagebox.showwarning("Error","User name cannot be empty.")
      


  username = Label(top, text="Username:", font=("Helevtica",12),justify="right",background="white")
  username.grid(row=1, column=1, pady=(30,10))
  entry1 = Entry(top, width=40,bd=2)
  entry1.grid(row=2, column=1, pady=10,)
  password = Label(top, text="Password:", font=("Helevtica",12),background="white")
  password.grid(row=3, column=1, pady=10)
  entry2 = Entry(top,width=40,bd=2,show="*")
  entry2.grid(row=4, column=1, pady=10,)

  register_btn = Button(top, bg="Lightcoral",fg="white", text="Register",font=("Helevtica",8),command=registerGUI.register)
  register_btn.grid(row=6, column=1,pady=4)
  submit_btn = Button(top, bg="Lightcoral",fg="white", text="Login",font=("Helevtica",8),command=login)
  submit_btn.grid(row=5, column=1,pady=20)

  photo2 =Image.open("welcomepic.png")
  resize = photo2.resize((230, 155), Image.ANTIALIAS)
  photo_new = ImageTk.PhotoImage(resize)
  photo_label = Label(image=photo_new,bg="white", justify="center")
  photo_label.grid(row=0, column=1, columnspan=1, pady=10, padx=240)

  top.mainloop()

login()




