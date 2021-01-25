from tkinter import *
import mysql.connector
from tkinter import messagebox as mb
from datetime import *
from PIL import Image
from PIL import ImageTk

db = mysql.connector.connect(
    user="lifechoices",
    password="@Lifechoices1234",
    host="localhost",
    database="",
    auth_plugin="mysql_native_password"
)

cursor = db.cursor()
cursor.execute("create database if not exists lifechoicesonline")
cursor.execute("use lifechoicesonline")
cursor.execute("CREATE TABLE IF NOT EXISTS time_in(full_name varchar(60) Default null, date date, logged_in time)")
db.commit()
cursor.execute("CREATE TABLE IF NOT EXISTS time_out(full_name varchar(60) Default null, date date, logged_out time)")
db.commit()


def show():
    pss.config(show="")

def showAdmin():  # Function to show admin
    Login.destroy()
    import admin_login


def login():  # Function to login
    usr = usrame.get()
    p = pss.get()
    sql = "select * from users where username=%s and password=%s"
    cursor.execute(sql, [(usr), (p)])
    datab = cursor.fetchall()
    db.commit()
    mb.showinfo("Message", "Login successfully")

    if datab:
        Login.destroy()
        login1 = datetime.now()
        y = login1.strftime("%H:%M:%S")
        dt = login1.strftime("%d/%m/%y")
        time1 = usr, str(dt),  str(y)
        comm_time1 = "INSERT INTO time_in(full_name, date, logged_in)VALUES (%s, %s, %s)"
        cursor.execute(comm_time1, time1)
        db.commit()

        phone = Tk()
        phone.title("Logout")
        phone.geometry("400x200")

        path = 'header.png'
        img = ImageTk.PhotoImage(Image.open(path))
        panel = Label(phone, image=img, width=400, bg="black")
        panel.place(x=0, y=0)

        mobile = Label(phone, text="Mobile Number", bg="black", fg="white")
        mobile.place(x=10, y=100)

        mobile_ent = Entry(phone)
        mobile_ent.place(x=130, y=100)

        def logg_out():

            logout = datetime.now()
            y = logout.strftime("%H:%M:%S")
            time1 = usr, str(dt), str(y)
            comm_time1 = "INSERT INTO time_out(full_name, date, logged_out)VALUES (%s, %s, %s)"
            cursor.execute(comm_time1, time1)
            db.commit()
            mb.showinfo("Login", "logout successful")
            phone.destroy()

        signOut = Button(phone, text="sign out", command=logg_out)
        signOut.place(x=180, y=160)

        # Center Gui to screen
        window_height = 200
        window_width = 400

        screen_width = phone.winfo_screenwidth()
        screen_height = phone.winfo_screenheight()

        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))

        phone.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        phone.configure(bg="black")
        phone.mainloop()

    else:
        mb.showerror("Unsuccessful", "Login failed")





def createUser():
    Login.destroy()
    import reg


Login = Tk()
Login.resizable(False, False)
Login.title("Login")


#Welcome intro
path = 'header.png'
img = ImageTk.PhotoImage(Image.open(path))
panel = Label(Login, image=img, width=400, bg="black")
panel.place(x=0, y=0)


usrlb = Label(Login, text="Username:",fg="white", bg="black")
passlb = Label(Login, text="Password:",fg="white", bg="black")
usrame = Entry(Login)
pss = Entry(Login, show='*')




btn = Button(Login, text="register", width=10, command=createUser)  # Button to create users

btnLogin = Button(Login, text="login", width=10, command=login)  # Button to login



shwPss = Checkbutton(Login, text="Show Password", command=show)
# Placing widgets for Login window
usrlb.place(x=10, y=120)
usrame.place(x=85, y=120)
passlb.place(x=10, y=170)
pss.place(x=85, y=170)
shwPss.place(x=265, y=145)
btn.place(x=100, y=230)
btnLogin.place(x=220, y=230)


#Center Gui to screen
window_height = 270
window_width = 400

screen_width = Login.winfo_screenwidth()
screen_height = Login.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

Login.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

Login.bind("<Control-a>", lambda i: showAdmin())
Login.configure(bg="black")
Login.geometry("400x270")
Login.mainloop()

