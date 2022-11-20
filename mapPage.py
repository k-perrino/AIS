#Import the required Libraries
from tkinter import *
from tkinter import ttk
#Create an instance of Tkinter frame

import mapData
import main
f = ("Times bold", 14)

def HomePage():
  #win = Tk()
  #Set the geometry of the Tkinter frame
  #win.geometry("750x250")
  #win.configure(bg = "Blue")
  #win.title("Map")
  
  main.root.destroy()
  import HomePage

frame_test = LabelFrame(main.root)
frame_test.grid(column=0,row=3,pady=20,padx=10)

test = Button(
    frame_test, 
    text="Home", 
    font=f,
    command=HomePage
    )
test.grid(column=0, row=3,pady=20, padx=10)