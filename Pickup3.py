#Import the required Libraries
from tkinter import *
from tkinter import ttk
win = Tk()
#Set the geometry of the Tkinter frame
win.geometry("750x250")
win.title("Pick Up Locations")
f = ("Times bold", 14)

#create the text on the screen
ttk.Label(win, text=("1-210-794-9544"), font = 'Courier').pack()
ttk.Label(win, text=("1-844-471-1052"), font = 'Courier').pack()
#create back button
def back():
    win.destroy
    import PickUp

Button(
    win, 
    text="Back", 
    font=f,
    command=back
    ).place(relx=0.5, rely=1, anchor=S)