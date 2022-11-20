#Import the required Libraries
from tkinter import *
from tkinter import ttk
#Create an instance of Tkinter frame
win = Tk()
#Set the geometry of the Tkinter frame
win.geometry("750x400")
win.configure(bg = "cyan")
win.title("Pick Up Locations")
f = ("Times bold", 14)

def HomePage():
    win.destroy
    import HomePage

def Pickup1():
    win.destroy
    import Pickup1
def Pickup2():
    win.destroy
    import Pickup2
def Pickup3():
    win.destroy
    import Pickup3
def Pickup4():
    win.destroy
    import Pickup4
def Pickup5():
    win.destroy
    import Pickup5
def Pickup6():
    win.destroy
    import Pickup6


Button(
    win, 
    text="Home", 
    font=f,
    command=HomePage
    ).place(relx=0.5, rely=1, anchor=S)

Button(
    win, 
    text="San Antonio Electronics and Computer Recycling Service", 
    font=f,
    command=Pickup1
    ).place(relx=0.5, rely=.1, anchor=CENTER)

Button(
    win, 
    text="United Electronic Recyling", 
    font=f,
    command=Pickup2
    ).place(relx=0.5, rely=.2, anchor=CENTER)
Button(
    win, 
    text="The Junkluggers of San Antonio", 
    font=f,
    command=Pickup3
    ).place(relx=0.5, rely=.3, anchor=CENTER)
Button(
    win, 
    text="R3ewaste", 
    font=f,
    command=Pickup4
    ).place(relx=0.5, rely=.4, anchor=CENTER)
Button(
    win, 
    text="All Green Recycling", 
    font=f,
    command=Pickup5
    ).place(relx=0.5, rely=.5, anchor=CENTER)
Button(
    win, 
    text="E-Cycle Enterprises", 
    font=f,
    command=Pickup6
    ).place(relx=0.5, rely=.6, anchor=CENTER)
win.mainloop()