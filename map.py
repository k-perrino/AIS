import pandas as pd, numpy as np
import requests
import json
import time
final_data = []
# Parameters

from tkinter import *
import tkintermapview
from tkinter import ttk
from tkinter import *
import tkintermapview
import requests
import urllib.parse
import googlemaps

API_KEY = 'AIzaSyDkX3to5XGb9ElI7AJ7ui83Gwz5p5kn-qY' #insert your Places API

map_client = googlemaps.Client(API_KEY)

address = '1 UTSA Circle, San Antonio, TX 78249'
url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'

#response = requests.get(url).json()
#coordinate = [str(response[0]["lat"]), str(response[0]["lon"])]
geocode = map_client.geocode(address=address)
(lat, lng) = map(geocode[0]['geometry']['location'].get, ('lat', 'lng'))

coordinate = ['29.589183','-98.627073']
keywords = ['Best Buy']

def miles_to_meters(miles):
    try:
        return miles * 1_609.344
    except:
        return 0
#https://maps.googleapis.com/maps/api/place/textsearch/json?query=coffee+shop&location=35.7790905,-78.642413&radius=2000&region=us&type=cafe,bakery&key=MY_API_KEY
radius = miles_to_meters(10)
name = ['Best+Buy', 'Staples']
for x in name:
    url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query='+str(x) + '&location=' + '{},{}'.format(coordinate[0],coordinate[1])+'&radius='+str(radius)+'&key='+str(API_KEY)
    params = {}
  
    res = requests.get(url, params = params)
    results =  json.loads(res.content)
    final_data.extend(results['results'])
    time.sleep(2)
    while "next_page_token" in results:
        params['pagetoken'] = results['next_page_token'],
        res = requests.get(url, params = params)
        results = json.loads(res.content)
        #print(str(results))
        final_data.extend(results['results'])
        time.sleep(2)
       


names = []
lats = []
lons = []
addresses = []
for x in range(len(final_data)):
    f = final_data[x]
    print(f['name'])
    if(f['name'] == "Geek Squad" or ("Wines" in f['name']) or f['name'] == 'Office Depot' or f['name'] == 'Dollar Tree' or f['name'] == 'Office Max'):
        continue
    addresses.append(f['formatted_address'])
    names.append(f['name'])
    lats.append(f['geometry']['location']['lat'])
    lons.append(f['geometry']['location']['lng'])

dict = {'name': names, 'latitude': lats, 'longitudes':lons, 'address': addresses}
df = pd.DataFrame(dict)
#df['url'] = 'https://www.google.com/maps/place/?q=place_id:' + df['place_id']

df.to_excel('test5.xlsx', index=False)
df.head()





