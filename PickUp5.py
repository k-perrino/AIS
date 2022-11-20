#Import the required Libraries
from tkinter import *
from tkinter import ttk
win = Tk()
#Set the geometry of the Tkinter frame
win.geometry("750x250")
win.title("Pick Up Locations")
f = ("Times bold", 14)

#create the text on the screen
ttk.Label(win, text=("2911 Turtle Creek Blvd., Suite 300"), font = 'Courier').pack()
ttk.Label(win, text=("Dallas, TX, 75219, US"), font = 'Courier').pack()
ttk.Label(win, text=("(214) 972-0076"), font = 'Courier').pack()
#create back button
def back():
    win.destroy
    import PickUpLocations5

Button(
    win, 
    text="Back", 
    font=f,
    command=back
    ).place(relx=0.5, rely=1, anchor=S)