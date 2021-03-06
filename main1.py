
from tkinter import *
from tkinter import messagebox as ms
from subprocess import call
import sqlite3
from tkinter import ttk

# make database and users (if not exists already) table at programme start up
with sqlite3.connect('quit.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL ,password TEX NOT NULL);')
db.commit()
db.close()

def click_checkout():
    call(["python", "PRODUCT.py"])
class main:
    def __init__(self, master):
        self.master = master
        # Some Usefull variables
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        # Create Widgets
        self.widgets()

    # Login Function
    def login(self):
        # Establish Connection
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()

        # Find user If there is any take proper action
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user, [(self.username.get()), (self.password.get())])
        result = c.fetchall()
        if result:
            self.logf.pack_forget()
            self.head['text'] = click_checkout()
            self.head['pady'] = 150
        else:
            ms.showerror('Oops!', 'Username Not Found.')

    def new_user(self):
        # Establish Connection
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()

        # Find Existing username if any take proper action
        find_user = ('SELECT * FROM user WHERE username = ?')
        c.execute(find_user, [(self.username.get())])
        if c.fetchall():
            ms.showerror('Error!', 'Username Taken Try a Diffrent One.')
        else:
            ms.showinfo('Success!', 'Account Created!')
            self.log()
        # Create New Account
        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        c.execute(insert, [(self.n_username.get()), (self.n_password.get())])
        db.commit()

        # Frame Packing Methords

    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()

    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()

    # Draw Widgets
    def widgets(self):
        self.head = Label(self.master, text='LOGIN', font=('', 35), pady=10,bg="#e6ffff")
        self.head.pack()
        self.logf = Frame(self.master, padx=10, pady=10,bg="#e6ffff")
        Label(self.logf, text='Username: ', font=('', 20), pady=5, padx=5,bg="#e6ffff").grid(sticky=W)
        Entry(self.logf, textvariable=self.username, bd=5, font=('', 15),bg="#e6ffff").grid(row=0, column=4)
        Label(self.logf, text='Password: ', font=('', 20), pady=5, padx=5,bg="#e6ffff").grid(sticky=W,row=5)
        Entry(self.logf, textvariable=self.password, bd=5, font=('', 15), show='*',bg="#e6ffff").grid(row=5, column=4)
        Button(self.logf, text=' Login ', bd=3, font=('', 15), padx=5, pady=5, command=self.login,bg="#e6ffff").grid(row=10)
        Button(self.logf, text=' Create Account ', bd=3, font=('', 15), padx=5, pady=5, command=self.cr,bg="#e6ffff").grid(row=10,column=4)
        self.logf.pack()
        self.logf
        

        self.crf = Frame(self.master, padx=10, pady=10,bg="#e6ffff")
        Label(self.crf, text='Username: ', font=('', 20), pady=5, padx=5,bg="#e6ffff").grid(sticky=W)
        Entry(self.crf, textvariable=self.n_username, bd=5, font=('', 15),bg="#e6ffff").grid(row=0, column=1)
        Label(self.crf, text='Password: ', font=('', 20), pady=5, padx=5,bg="#e6ffff").grid(sticky=W)
        Entry(self.crf, textvariable=self.n_password, bd=5, font=('', 15), show='*',bg="#e6ffff").grid(row=1, column=1)
        Button(self.crf, text='Create Account', bd=3, font=('', 15), padx=5, pady=5, command=self.new_user,bg="#e6ffff").grid()
        Button(self.crf, text='Go to Login', bd=3, font=('', 15), padx=5, pady=5, command=self.log,bg="#e6ffff").grid(row=2,
                                                                                                         column=1)


# create window and application object
root = Tk()
root.state("zoomed")
root.configure(bg="#e6ffff")


# root.title("Login Form")
main(root)
root.mainloop()
