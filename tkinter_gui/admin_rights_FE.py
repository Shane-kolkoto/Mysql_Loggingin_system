import mysql.connector
from tkinter import *
from tkinter import messagebox as mb
from tkinter import *
from PIL import ImageTk, Image
import datetime
import os


db = mysql.connector.connect(
    user="root",
    password="Shane3004#",
    host="localhost",
    database="lifechoicesonline",
    auth_plugin="mysql_native_password"
)

cursor = db.cursor()

def display():
    selction = var.get()
    if selction == 1:
        cursor.execute("SELECT id FROM admin")

        id = cursor.fetchall()

        for x in id:
            liName.insert(END, x)

        liName.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT full_name FROM admin")

        name = cursor.fetchall()

        for x in name:
            liD.insert(END, x)

        liD.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT username FROM admin")

        uName = cursor.fetchall()
        for x in uName:
            liT.insert(END, x)
        liT.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT password FROM admin")

        pas = cursor.fetchall()
        for x in pas:
            liP.insert(END, x)
        liP.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT username FROM time_reg")

        tUn = cursor.fetchall()
        for x in tUn:
            Liu.insert(END, x)
        Liu.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT date FROM time_reg")

        d = cursor.fetchall()
        for x in d:
            Lid.insert(END, x)
        Lid.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT login_time FROM time_reg")

        timeIn = cursor.fetchall()
        for x in timeIn:
            LiTi.insert(END, x)
        LiTi.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT logout_time FROM time_out")

        timeout = cursor.fetchall()
        for x in timeout:
            LiT0.insert(END, x)
        LiT0.insert(END, str(cursor.rowcount) + " rows")

    elif selction == 2:
        cursor.execute("SELECT id FROM users")

        id = cursor.fetchall()

        for x in id:
            liName.insert(END, x)

        liName.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT full_name FROM users")

        name = cursor.fetchall()

        for x in name:
            liD.insert(END, x)

        liD.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT username FROM users")

        uName = cursor.fetchall()
        for x in uName:
            liT.insert(END, x)
        liT.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT password FROM users")

        pas = cursor.fetchall()
        for x in pas:
            liP.insert(END, x)
        liP.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT username FROM time_reg")

        tUn = cursor.fetchall()
        for x in tUn:
            Liu.insert(END, x)
        Liu.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT date FROM time_reg")

        d = cursor.fetchall()
        for x in d:
            Lid.insert(END, x)
        Lid.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT login_time FROM time_reg")

        timeIn = cursor.fetchall()
        for x in timeIn:
            LiTi.insert(END, x)
        LiTi.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT logout_time FROM time_out")

        timeIn = cursor.fetchall()
        for x in timeIn:
            LiT0.insert(END, x)
        LiT0.insert(END, str(cursor.rowcount) + " rows")

def add():
    selction = var.get()
    if selction == 1:
        comm3 = "INSERT INTO admin (full_name, username, password) VALUES (%s, %s, %s)"
        user_info1 = str(nameReg.get()), str(usrName.get()), psswrd.get()
        cursor.execute(comm3, user_info1)
        db.commit()
        mb.showinfo("Confirmation", "Admin created successfully")

    elif selction == 2:
        comm3 = "INSERT INTO users (full_name, username, password) VALUES (%s, %s, %s)"
        user_info1 = str(nameReg.get()), str(usrName.get()), psswrd.get()
        cursor.execute(comm3, user_info1)
        db.commit()
        mb.showinfo("Confirmation", "User created successfully")


def delete():
    selction = var.get()
    if selction == 1:
        fullname=usrName.get()
        Delete="delete from admin where full_name='%s'" %(fullname)
        cursor.execute(Delete)
        db.commit()
        mb.showinfo("Information","Record Deleted")

    elif selction == 2:
        fullname = usrName.get()
        Delete = "delete from users where full_name='%s'" % (fullname)
        cursor.execute(Delete)
        db.commit()
        mb.showinfo("Information", "Record Deleted")

def clear():
    liName.delete(0,END)
    liD.delete(0,END)
    liT.delete(0,END)
    liP.delete(0,END)
    Liu.delete(0, END)
    Lid.delete(0,END)
    LiTi.delete(0, END)
    LiT0.delete(0,END)



def grant():
    selection = var.get()
    if selection == 1:
        u = usrName.get()
        priv_com = "GRANT ALL PRIVILEGES ON books.authors  TO '%s'@'localhost'" % (u)
        cursor.execute(priv_com)
        mb.showinfo("Message", "Privileges Granted")
    elif selection >=2:
        mb.showerror("Attention", "Admin users online")

def count():

    selection = var.get()
    if selection == 1:
        cursor = db.cursor()
        query = "SELECT count(*) FROM admin"
        cursor.execute(query)
        myresult = cursor.fetchall()
        total = ('Total number of admin users logged in\n',(myresult[-1][-1]))
        mb.showinfo("Attention", total)
    elif selection == 2:
        cursor = db.cursor()
        query = "SELECT count(*) FROM users"
        cursor.execute(query)
        myresult = cursor.fetchall()
        total = ('Total number of users logged in\n', (myresult[-1][-1]))
        mb.showinfo("Attention", total)

def dump():
    pass


admin = Tk()
admin.resizable(False, False)
admin.title("Admin Page")

pic = '../images/header.png'
img1 = ImageTk.PhotoImage(Image.open(pic))
panel = Label(admin, image=img1, width=800, bg="black")
panel.place(x=20, y=0)





liLb = Label(admin, text="ID:", fg="white", bg="black")
liName = Listbox(admin, width=20)
li2Lb = Label(admin, text="Fullname:", fg="white", bg="black")
liD = Listbox(admin, width=20)
liTL = Label(admin, text="Username", fg="white", bg="black")
liT = Listbox(admin, width=20)
liLp = Label(admin, text="Password:",fg="white", bg="black")
liP = Listbox(admin, width=20)


#######################################
lbU = Label(admin, text="Username:",fg="white", bg="black")
Liu = Listbox(admin, width=20)
lbD = Label(admin, text="Date:", fg="white", bg="black")
Lid = Listbox(admin, width=20)
LiTiL = Label(admin, text="Login Time:", fg="white", bg="black")
LiTi = Listbox(admin, width=20)
LiOl = Label(admin, text="Logout Time:", fg="white", bg="black")
LiT0 = Listbox(admin, width=20)


#Entries
nameRegLb = Label(admin, text="Full Name:",fg="white", bg="black")
nameReg = Entry(admin)
usrNamelb = Label(admin, text="Username:",fg="white", bg="black")
psswrdlb = Label(admin, text="Password:",fg="white", bg="black")

usrName = Entry(admin)
psswrd = Entry(admin, show='*')



liLb.place(x=260, y=100)
liName.place(x=260, y=130)
li2Lb.place(x=390, y=100)
liD.place(x=390, y=130)
liTL.place(x=520, y=100)
liT.place(x=520, y=130)
liLp.place(x=650, y=100)
liP.place(x=650, y=130)
lbU.place(x=260, y=320)
Liu.place(x=260, y=350)
lbD.place(x=390, y=320)
Lid.place(x=390, y=350)
LiTiL.place(x=520, y=320)
LiTi.place(x=520, y=350)
LiOl.place(x=650, y=320)
LiT0.place(x=650, y=350)

nameRegLb.place(x=10, y=190)
nameReg.place(x=90, y=190)
usrNamelb.place(x=10, y=240)
usrName.place(x=90, y=240)
psswrdlb.place(x=10, y=290)
psswrd.place(x=90, y=290)


#Buttons
showbtn = Button(admin, text="Display",width=5, command=display, bd=2)
addbtn = Button(admin, text="Add", width=5, bd=2, command=add)
removebtn = Button(admin, text="Delete", width=5, bd=2, command=delete)
updatebtn = Button(admin, text="Clear", width=5, bd=2, command=clear)
grantbtn = Button(admin, text="Grant", width=5, bd=2, command=grant)
quitbtn = Button(admin, text="Count", width=5, bd=2, command=count)
backup = Button(admin, text="Back-up", width=22, bg="red", fg="white", command=dump)
showbtn.place(x=20, y=350)
addbtn.place(x=80, y=350)
removebtn.place(x=140, y=350)
updatebtn.place(x=20, y=390)
grantbtn.place(x=80, y=390)
quitbtn.place(x=140, y=390)
backup.place(x=20, y=430)


var = IntVar()
admin_radio = Radiobutton(admin, text="admin", variable=var, value=1, fg="white", bg="black")
admin_radio.place(x=10, y=150)


user_radio = Radiobutton(admin, text="Users", variable=var, value=2, fg="white", bg="black")
user_radio.place(x=100, y=150)



#Center gui on screen
window_height = 600
window_width = 800

screen_width = admin.winfo_screenwidth()
screen_height = admin.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

admin.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
admin.geometry("800x600")
admin.configure(bg="black")
admin.mainloop()