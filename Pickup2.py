#Import the required Libraries
from tkinter import *
from tkinter import ttk
win = Tk()
#Set the geometry of the Tkinter frame
win.geometry("750x250")
win.title("Pick Up Locations")
f = ("Times bold", 14)

#create the text on the screen
ttk.Label(win, text=("505 Airline Dr"), font = 'Courier').pack()
ttk.Label(win, text=("Coppell, TX 75019"), font = 'Courier').pack()
ttk.Label(win, text=("Phone: (855) 837-8326"), font = 'Courier').pack()
ttk.Label(win, text=("Fax: (855) 522-0812"), font = 'Courier').pack()
ttk.Label(win, text=("Email: info@uerteam.com"), font = 'Courier').pack()
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