from URLs import *
import requests

GOOGLE_MAPS_API_URL = 'http://maps.googleapis.com/maps/api/geocode/json'

class location:

    def google_latlong_finder(self, address):

        params = {'address': address, 'sensor': 'false', 'region': 'uk'}
        req = requests.get(GOOGLE_MAPS_API_URL, params=params)
        res = req.json()
        print(res)
        result = res['results'][0]
        geodata = dict()
        geodata['lat'] = result['geometry']['location']['lat']
        geodata['lng'] = result['geometry']['location']['lng']
        return geodata


    def google_address_finder(self, latlong):

        params = {'latlng': latlong, 'sensor' : 'false', 'region' : 'uk'}
        req = requests.get(GOOGLE_MAPS_API_URL, params=params)
        res = req.json()
        result = res['results'][0]
        geodata = dict()
        geodata['address'] = result['formatted_address']
        return geodata

    def mapbox_finder(self, address):
        pass

    def graph_hopper_finder(self, address):
        pass


test = location()
my_address = test.google_latlong_finder("battersea park")
print(my_address)