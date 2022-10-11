from random import Random
import random
from secrets import choice


import random
from tkinter import *
from tkinter import messagebox

lowercase_letters = "abcdefghijklmnopqrstuwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUWXYZ"
numbers = "0123456789"
simbols = "@#$%&*/\?"

Use_for = lowercase_letters + uppercase_letters + numbers + simbols
password_length = 10

password = "".join(random.sample(Use_for, password_length))

#print("Your password is: " + password)

messagebox.showinfo("Password", "Your password is: " + password)

def ppp():
    #print("¿Create a file?")
    question = messagebox.askquestion("Password", "¿Create a file with your password?")
    if question == 'yes':  
        #print("CREATING FILE...")
        record = open("password.txt", "w")
        record.write(password)  
        #print("¡FILE CREATED!")
        messagebox.showinfo("Password", "A file called password.txt has been created")
ppp()


