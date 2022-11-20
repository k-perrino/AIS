#Import the required Libraries
from tkinter import *
from tkinter import ttk
#Create an instance of Tkinter frame
win = Tk()
#Set the geometry of the Tkinter frame
win.geometry("750x250")
win.configure(bg = "Blue")
win.title("Home Page")
f = ("Times bold", 14)

def Whatis():
    win.destroy()
    import WhatIs
def mapPage():
    win.destroy()
    import mapPage
def PickUp():
    win.destroy()
    import PickUp

Button(
    win, 
    text="Drop off Locations", 
    font=f,
    command=mapPage
    ).place(relx=0.5, rely=0.3, anchor=CENTER)

Button(
    win, 
    text="Pick Up Locations", 
    font=f,
    command=PickUp
    ).place(relx=.5, rely=.5, anchor=CENTER)

Button(
    win, 
    text="What is e-waste", 
    font=f,
    command=Whatis
    ).place(relx=.5, rely=.7, anchor=CENTER)

win.mainloop()