"""
Step 1: Create table
Step 2: Prompt user for Login or Sign Up details ( username, password, email)
Step 3: Select from or Insert into table
Step 4: Check if user exist
Step 5: Display appropriate message
"""
import sqlite3
import tkinter

db = sqlite3.connect("user_details.db")
c = db.cursor()
c.execute("CREATE TABLE IF NOT EXISTS users "
          "(id INTEGER PRIMARY KEY , name TEXT NOT NULL, password TEXT NOT NULL)")


def login():
    username = username_entry.get()
    password = password_entry.get()
    c.execute("SELECT name FROM users WHERE name=? AND password= ? ", (username, password))
    user = c.fetchone()

    if username == '' or password == '':
        tkinter.Label(head_frame, text='Please enter a username and password ', fg="red").grid(row=1, column=1)
    elif user is None:
        tkinter.Label(head_frame, text='Sorry we couldn\'t find you ', fg="red").grid(row=1, column=1)
        tkinter.Label(head_frame, text='or password is incorrect', fg="red").grid(row=2, column=1)
    else:
        print_message("Welcome Back {}!", username)


def signup():
    username = username_entry.get()
    password = password_entry.get()
    c.execute("SELECT * FROM users")
    user = None

    for user in c.fetchall():
        if user[1] == username:
            user = user

    if username == '' or password == '':
        tkinter.Label(head_frame, text='Please enter a username and password ', fg="red").grid(row=1, column=1)
    elif user is None:
        c.execute("INSERT INTO users (name, password) VALUES (?,?)", (username, password))
        print_message("You have been registered {}! Thank you", username)
    else:
        tkinter.Label(head_frame, text='Username is already used', fg="red").grid(row=1, column=1)


def print_message(message, user):
    head_frame.destroy()
    username_frame.destroy()
    password_frame.destroy()
    button_frame.destroy()
    tkinter.Label(mainWindow, text=message.format(user), font=("Helvetica", 10)).grid(row=0, column=1)
    mainWindow.minsize(width='340', height='280')
    mainWindow.maxsize(width='340', height='280')


mainWindow = tkinter.Tk()
mainWindow.title('Login')
mainWindow.geometry("240x280+600+200")
mainWindow.minsize(width='240', height='280')
mainWindow.maxsize(width='240', height='280')
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=3)
mainWindow.columnconfigure(2, weight=1)


# Header
head_frame = tkinter.Frame(mainWindow)
head_frame.grid(row=0, column=0, columnspan=3)
head_frame['pady'] = 10

head_variable = tkinter.StringVar()
head_variable.set("Login")
head_label = tkinter.Label(head_frame, textvariable=head_variable, font=("Helvetica", 30)).grid(row=0, column=1)

# Username section
username_frame = tkinter.Frame(mainWindow)
username_frame.grid(row=1, column=1)
username_frame['pady'] = 5

username_label = tkinter.Label(username_frame, text="Username")
username_label.grid(row=0, column=0, sticky='w')

username_entry = tkinter.Entry(username_frame)
username_entry.grid(row=1, column=0, sticky='ew')

# Password section
password_frame = tkinter.Frame(mainWindow)
password_frame.grid(row=2, column=1)
password_frame['pady'] = 5

password_label = tkinter.Label(password_frame, text="Password")
password_label.grid(row=0, column=0, sticky='w')

password_entry = tkinter.Entry(password_frame)
password_entry.grid(row=1, column=0, sticky='ew')

# Button section
button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=1)
button_frame['pady'] = 10

button1_variable = tkinter.StringVar()
button1_variable.set('Login')
button1 = tkinter.Button(button_frame, textvariable=button1_variable, command=login, width=6)
button1.grid(row=0, column=0, padx=(0, 10))

button2_variable = tkinter.StringVar()
button2_variable.set('SignUp')
button2 = tkinter.Button(button_frame, textvariable=button2_variable, command=signup, width=6)
button2.grid(row=0, column=1, padx=(10, 0))

mainWindow.mainloop()
db.commit()
