import requests
import json
import time
import pandas as pd
import tkintermapview
import googlemaps
from math import radians, cos, sin, asin, sqrt

address = ''

def convertDistance(lon1, lat1, lon2, lat2):
  # convert decimal degrees to radians 
  lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

  # haversine formula 
  dlon = lon2 - lon1 
  dlat = lat2 - lat1 
  a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
  c = 2 * asin(sqrt(a)) 
  r = 3956 # Radius of earth
  return c * r

def miles_to_meters(miles):
  try:
    return miles * 1_609.344
  except:
    return 0
      
def main():

  global coord
  global lat
  global lng
  
  collected_data = []
  API_KEY = 'AIzaSyDkX3to5XGb9ElI7AJ7ui83Gwz5p5kn-qY'
  map_client = googlemaps.Client(API_KEY)
  print(address)
  geocode = map_client.geocode(address=address)
  (lat, lng) = map(geocode[0]['geometry']['location'].get, ('lat', 'lng'))
  coord = (lat,lng)
  radius = miles_to_meters(5)
  milesRadius = 5
  name = ['Best+Buy', 'Staples']
  for x in name:
    url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query='+str(x) + '&location=' + '{},{}'.format(lat,lng)+'&radius='+str(radius)+'&key='+str(API_KEY)
    params = {}
    res = requests.get(url, params = params)
    results =  json.loads(res.content)
    collected_data.extend(results['results'])
    time.sleep(2)
    while "next_page_token" in results:
      params['pagetoken'] = results['next_page_token'],
      res = requests.get(url, params = params)
      results = json.loads(res.content)
      collected_data.extend(results['results'])
      time.sleep(2)

  names = []
  lats = []
  lons = []
  addresses = []
  #check if City drop off is in radius
  lat1 = 29.4517390987526
  lng1 = -98.628115271826
  b = convertDistance(lat, lng, lat1, lng1)
  if(b<=milesRadius):
    addresses.append('7030 Culebra Road, San Antonio, TX 78238')
    names.append('City of San Antonio Drop Off')
    lats.append(lat1)
    lons.append(lng1)
  for x in range(len(collected_data)):
    f = collected_data[x]
      #print(type(f['geometry']['location']['lat']))
    
    if(f['name'] == 'Best Buy' or f['name'] =='Staples'):
      a = convertDistance(lat, lng, (f['geometry']['location']['lat']), (f['geometry']['location']['lng']))
      #print(a)
      if(a <= milesRadius):
        addresses.append(f['formatted_address'])
        names.append(f['name'])
        lats.append(f['geometry']['location']['lat'])
        lons.append(f['geometry']['location']['lng'])

  dict = {'name': names, 'latitude': lats, 'longitude':lons, 'address': addresses}
  df = pd.DataFrame(dict)
  df.to_csv('test.csv', index=False)
  return df



if __name__ == "__main__":
  main()