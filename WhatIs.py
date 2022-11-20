#Import the required Libraries
from tkinter import *
from tkinter import ttk
#Create an instance of Tkinter frame
win = Tk()
#Set the geometry of the Tkinter frame
win.geometry("760x350")
win.configure(bg = "Blue")
win.title("What is E-waste")
f = ("Times bold", 14)

ttk.Label(win, text=("Why?"), font = 'Courier').pack()
ttk.Label(win, text=("The improper handling of electronic e-waste (electronic waste) has led to "), font = 'Courier').pack()
ttk.Label(win, text=("much human and environmental harm. The toxic metals from the waste has "), font = 'Courier').pack()
ttk.Label(win, text=("rendered soil and ater bodies toxic for wildlife and has caused "), font = 'Courier').pack()
ttk.Label(win, text=("irreversible health effects to people, like cancer and neurological damages."), font = 'Courier').pack()
ttk.Label(win, text=("Who?"), font = 'Courier').pack()
ttk.Label(win, text=("Many organizations have come forth to advocate and enforce better disposal "), font = 'Courier').pack()
ttk.Label(win, text=("of electronic waste, such as the United States Environmental Protection "), font = 'Courier').pack()
ttk.Label(win, text=("Agency and Taiwan Environmental Protection Administration, coming together "), font = 'Courier').pack()
ttk.Label(win, text=("as the International E-Waste Management Network to face this problem."), font = 'Courier').pack()
ttk.Label(win, text=("What?"), font = 'Courier').pack()
ttk.Label(win, text=("By giving e-waste to the correct facilities and not throwing it away in the "), font = 'Courier').pack()
ttk.Label(win, text=("garbage, recycling companies can safely remove precious and toxic metals "), font = 'Courier').pack()
ttk.Label(win, text=("from the materials for intended disposal. "), font = 'Courier').pack()





def HomePage():
    win.destroy
    import HomePage2

Button(
    win, 
    text="Home", 
    font=f,
    command=HomePage
    ).place(relx=0.5, rely=1, anchor=S)
win.mainloop()