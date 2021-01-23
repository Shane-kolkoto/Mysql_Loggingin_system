# Register System with Python GUI and MySQL
import mysql.connector
from tkinter import messagebox as mb
from tkinter import *
from PIL import ImageTk, Image
from datetime import *
import os

db = mysql.connector.connect(
    user="root",
    password="Shane3004#",
    host="localhost",
    database="lifechoicesonline",
    auth_plugin="mysql_native_password"
)

cursor = db.cursor()


admin_login = Tk()
admin_login.resizable(False, False)
admin_login.title("Admin")


#Welcome intro
pic = '../images/header.png'
img1 = ImageTk.PhotoImage(Image.open(pic))
panel = Label(admin_login, image=img1, width=400, bg="black")
panel.place(x=20, y=0)








def login():
    usr = usrEnt.get()
    p = adUps.get()
    sql = "select * from admin where username=%s and password=%s"
    cursor.execute(sql, [(usr), (p)])
    datab = cursor.fetchall()

    if datab:
        mb.showinfo("Login", "login successful")
        admin_login.destroy()
        import tkinter_gui.admin_rights_FE
    else:
        mb.showerror("Unsuccessful", "Login failed")

def back():
    admin_login.destroy()
    import tkinter_gui.main



logBtn = Button(admin_login, text="Back", command=back)
privBtn = Button(admin_login, text="Login", command=login)

usrAdLb = Label(admin_login, text="User/Admin Name:", fg="white", bg="black")
usrEnt = Entry(admin_login)
usrAdp = Label(admin_login, text="Password", fg="white", bg="black")
adUps = Entry(admin_login)
usrAdLb.place(x=20, y=100)
usrEnt.place(x=150, y=100)
usrAdp.place(x=20, y=140)
adUps.place(x=150, y=140)
privBtn.place(x=20, y=180)
logBtn.place(x=320, y=180)



#Center gui on screen
window_height = 240
window_width = 400

screen_width = admin_login.winfo_screenwidth()
screen_height = admin_login.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

admin_login.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
admin_login.geometry("400x240")
admin_login.configure(bg="black")
admin_login.mainloop()


