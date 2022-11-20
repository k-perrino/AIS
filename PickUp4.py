#Import the required Libraries
from tkinter import *
from tkinter import ttk
win = Tk()
#Set the geometry of the Tkinter frame
win.geometry("750x250")
win.title("Pick Up Locations")
f = ("Times bold", 14)

#create the text on the screen
ttk.Label(win, text=("2216 Rutland Drive, Suite B"), font = 'Courier').pack()
ttk.Label(win, text=("Austin, TX 78758"), font = 'Courier').pack()
#create back button
def back():
    win.destroy
    import PickUpLocations4

Button(
    win, 
    text="Back", 
    font=f,
    command=back
    ).place(relx=0.5, rely=1, anchor=S)