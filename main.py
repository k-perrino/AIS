import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy_garden.mapview import MapView

class MyApp(App):

    def build(self):
        return Label(text='Hello world')

class MapViewApp(App):
    def build(self):
        mapview = MapView(zoom=11, lat=50.6394, lon=3.057)
        return mapview


if __name__ == '__main__':
    #MyApp().run()
    MapViewApp().run()
