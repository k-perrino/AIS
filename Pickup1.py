#Import the required Libraries
from tkinter import *
from tkinter import ttk
win = Tk()
#Set the geometry of the Tkinter frame
win.geometry("750x250")
win.title("Pick Up Locations")
f = ("Times bold", 14)

#create the text on the screen
ttk.Label(win, text=("STS Electronic Recycling - An Inc. 5000 Company"), font = 'Courier').pack()
ttk.Label(win, text=("1777 NE loop 410 Suite 600"), font = 'Courier').pack()
ttk.Label(win, text=("San Antonio, TX 78217"), font = 'Courier').pack()
ttk.Label(win, text=("210-841-5704"), font = 'Courier').pack()

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