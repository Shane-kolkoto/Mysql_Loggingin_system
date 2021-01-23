from tkinter import *
import mysql.connector
from tkinter import messagebox as mb
from datetime import *
import PIL, ImageTk, Image



reg = Tk()
reg.title("Create student")
reg.resizable(False, False)



db = mysql.connector.connect(
    user="root",
    password="Shane3004#",
    host="localhost",
    database="lifechoicesonline",
    auth_plugin="mysql_native_password"
)

cursor = db.cursor()

def show():
    psswrd.config(show="")

#Welcome intro
path = '../images/header.png'
img = ImageTk.PhotoImage(Image.open(path))
panel = Label(reg, image=img, width=400, bg="black")
panel.place(x=0, y=0)


nameRegLb = Label(reg, text="Full Name:",fg="white", bg="black")
nameReg = Entry(reg)
usrNamelb = Label(reg, text="Username:",fg="white", bg="black")
psswrdlb = Label(reg, text="Password:",fg="white", bg="black")

usrName = Entry(reg)
psswrd = Entry(reg, show='*')

def addUser():
    try:
        user_info = (nameReg.get(), str(usrName.get()), str(psswrd.get()))
        comm = "INSERT INTO users (full_name, username, password) VALUES (%s, %s, %s)"

        cursor.execute(comm, user_info)

        db.commit()
        mb.showinfo("Confirmation", "User Created Successfully")
        reg.destroy()
        import tkinter_gui.main

    except:
        mb.showerror("error", "Username already exist")
    reg.destroy()

def back():
    reg.destroy()
    import tkinter_gui.main

cBtn = Button(reg, text="Create student", command=addUser)
bBtn = Button(reg, text="Back", command=back)
shwPss = Checkbutton(reg, text="Show Password", command=show, fg="white", bg="black")

nameRegLb.place(x=10, y=100)
nameReg.place(x=90, y=100)
usrNamelb.place(x=10, y=140)
usrName.place(x=90, y=140)
psswrdlb.place(x=10, y=180)
psswrd.place(x=90, y=180)
cBtn.place(x=10, y=220)
bBtn.place(x=350, y=220)
shwPss.place(x=250, y=140)


#Center Gui to screen
window_height = 270
window_width = 400

screen_width = reg.winfo_screenwidth()
screen_height = reg.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

reg.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))


reg.config(bg="black")
reg.geometry("400x270")
reg.mainloop()