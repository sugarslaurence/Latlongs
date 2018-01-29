from pprint import pprint as pp
import googlemaps
from ApiKeys import *
import math

class distance_calculator:

    def get_distance_google(self, shipFrom, shipTo):
        gmaps = googlemaps.Client(key_distance)
        my_distance = gmaps.distance_matrix(shipFrom, shipTo)
        rows = my_distance["rows"][0]["elements"][0]
        distance_meters = rows["distance"]["value"]
        duration_minutes = rows["duration"]["value"]
        origin = my_distance["origin_addresses"]
        destination = my_distance["destination_addresses"]
        return {"distance" : distance_meters, "duration" : duration_minutes, "shipFrom" : origin, "shipTo": destination}


    def get_distance_haversine(self, shipFrom, shipTo):
        x = shipFrom.split(",")
        y = shipTo.split(",")
        lat1 = float(x[0])
        lon1 = float(x[1])
        lat2 = float(y[0])
        lon2 = float(y[1])
        radius = 6371 # km
        dlat = math.radians(lat2-lat1)
        dlon = math.radians(lon2-lon1)
        a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
            * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        haversine_distance = radius * c
        rounded_haversine_distance_in_meters = round(haversine_distance * 1000, -1)
        return rounded_haversine_distance_in_meters

    def haversine_google_difference(self, haversine, google):
        one = int(haversine)
        two = int(google)
        diff = abs(haversine - google)
        return diff

    def latlong_finder(self, shippingAddress):
        pass
