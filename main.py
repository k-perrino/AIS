from tkinter import Button, LabelFrame, CENTER, HORIZONTAL, Entry, Frame, NSEW, Text, Tk
from tkinter import *
import tkintermapview
import tkinter as tk
import pandas as pd
from scipy import spatial
import mapData as md
import time

root = Tk()
root.title('E-WASTE')

#root.iconbitmap('c:/gui/codemy.ico')
root.geometry("700x700")
markerArr = []
address_array = []

bottom_frame = LabelFrame(root)
bottom_frame.grid(column=0,row=1,sticky=NSEW)

top_frame = LabelFrame(root)
top_frame.grid(column=0,row=0,sticky=NSEW)

map_widget = tkintermapview.TkinterMapView(bottom_frame,
                                           width=600,
                                           height=450,
                                           corner_radius=0)

map_widget.set_tile_server(
  "https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
map_widget.set_position(29.585171, -98.617249)

T = Text(top_frame, height=4, width=20)

def getData():
  global df
  data = pd.read_csv(r'test.csv')
  df = pd.DataFrame(data, columns=['name', 'latitude', 'longitude', 'address'])
  #return df
  
def sub():
  global coord
  global lat
  global lng
  print("Testing", adr_entry.get())
  md.address = adr_entry.get()
  md.main()
  time.sleep(15)
  getData()
  lat = md.lat
  lng = md.lng
  coord = (lat, lng)
  map_widget.set_position(lat,lng)
  
  
  
def makeMap():
  # Iterate all rows using DataFrame.iterrows():
  for index, row in df.iterrows():
    #print(index, row["latitude"], row["longitude"])
    markerArr.append(
      map_widget.set_marker(row["latitude"], row["longitude"], text = row["name"]))

    
def clear_marker_event():
  T.delete("1.0","end")
  map_widget.set_zoom(10)
  for marker in markerArr:
    marker.delete()
          
def find_closest_marker():
  coord_list = list(zip(df["latitude"], df["longitude"]))
  tree = spatial.KDTree(coord_list)
  d,i = (tree.query([(lat,lng)]))
  print(coord_list[i[0]][0])
  map_widget.set_position(coord_list[i[0]][0], coord_list[i[0]][1])
  map_widget.set_zoom(15)

def show_address_event(coords):
  adr = tkintermapview.convert_coordinates_to_address(coords[0], coords[1])
  T.delete("1.0","end")
  T.grid(column=4,row=0,pady=20,padx=10)
  T.insert(tk.END, "Address: %s %s %s %s, %s\n" % (adr.street, adr.housenumber, adr.postal, adr.city, adr.state))
  print("Nearby Address", adr.street, adr.housenumber, adr.postal, adr.city,
        adr.state, adr.country)


map_widget.add_right_click_menu_command(label="Show address",
                                        command=show_address_event,
                                        pass_coords=True)

# Set A Zoom Level
map_widget.set_zoom(10)
map_widget.grid(column=0,row=0,padx=30,pady=10,sticky=(NSEW))

frame_input = LabelFrame(root)
frame_input.grid(column=0,row=2,pady=20,padx=15)

adr_entry = Entry(frame_input, width=50,font=("Helvetica", 13))
adr_entry.grid(column=0,row=2,pady=10,padx=15)

submit_adr = Button(frame_input, text="SUBMIT", command=sub)
submit_adr.grid(column=1, row=2, pady=10,padx=10)

clear_button = Button(top_frame, text="CLEAR MARKERS", command=clear_marker_event)
clear_button.grid(column=1, row=0, pady=20, padx=10)

button = Button(top_frame, text="GENERATE", command=lambda: [makeMap(), find_closest_marker()])
button.grid(column=2, row=0, pady=10, padx=20)

root.mainloop()
