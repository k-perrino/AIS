#Import the required Libraries
from tkinter import *
from tkinter import ttk
win = Tk()
#Set the geometry of the Tkinter frame
win.geometry("750x250")
win.title("Pick Up Locations")
f = ("Times bold", 14)

#create the text on the screen
ttk.Label(win, text=("E-Cycle Enterprises"), font = 'Courier').pack()
ttk.Label(win, text=("2512 Program"), font = 'Courier').pack()
ttk.Label(win, text=("Drive STE #108"), font = 'Courier').pack()
ttk.Label(win, text=("Dallas, TX 75220"), font = 'Courier').pack()
ttk.Label(win, text=("885-317-5167"), font = 'Courier').pack()

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






