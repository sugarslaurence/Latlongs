from Distance import *
from GeoCoding import *
from Optimise import *
from Time import *

def distance_google(shipFrom, shipTo):  # Retrieves the GoogleAPI distance between two locations
    retrieve_distance = distance_calculator()
    distance = retrieve_distance.get_distance_google(shipFrom, shipTo)
    return distance

def distance_haversine(shipFrom, shipTo):  # Retrieves the Haversine distance between two locations
    retrieve_distance = distance_calculator()
    distance = retrieve_distance.get_distance_haversine(shipFrom, shipTo)
    return distance

def time_mapbox_matrix(shipFrom, shipTo):   # Retrieves the Mapbox time between two locations
    shipFromLongLat = long_lat(shipFrom)
    shipToLongLat = long_lat(shipTo)
    retrieve_time = time_calculator()
    time = retrieve_time.get_time_mapbox(shipFromLongLat, shipToLongLat)
    if time is None:
        return 0.0
    return time

def haversine_google_diff(shipFrom, shipTo):    # Retrieves distance difference from two locations between haversine and google API
    retrieve_distance = distance_calculator()
    distance = retrieve_distance.haversine_google_difference(shipFrom, shipTo)
    return distance

def get_lat_long_google(shippingAddress):      # Geocoding
    retrieve_latlong = location()
    lat_long = retrieve_latlong.google_latlong_finder(shippingAddress)
    return lat_long

def get_address_google(latLong):       # Reverse Geocoding
    retrieve_address = location()
    address = retrieve_address.google_address_finder(latLong)
    return address

def optimise(latlongs):     # Finds optimal trip between set of latlongs
    retrieve_trip = optimise()
    longlats = long_lats(latlongs)
    trip = retrieve_trip.map_box_optimise(longlats)
    return trip

def time_city_mapper(shipFrom, shipTo):
    CMshipFrom = lat_long_for_city_mapper(shipFrom)
    CMShipTo = lat_long_for_city_mapper(shipTo)
    retrieve_time = time_calculator()
    time = retrieve_time.get_time_city_mapper(CMshipFrom, CMShipTo)
    return time

######************************************************** UTILITIES *****************************************************#####

def haversine_google_difference(haversine, google):         # Find difference between Haversine and Google
    one = int(haversine)
    two = int(google)
    diff = abs(haversine - google)
    return diff

def long_lats(latlongs):    # Converts List LatLongs to LongLats
    longlats = ""
    for latlong in latlongs:
        x = latlong.split(",")
        lat, long = x[0].strip("\n"), x[1].strip("\n")
        if latlong == latlongs[-1]:
            longlats += long
            longlats += ","
            longlats += lat
        else:
            longlats += long + "," + lat + ";"
    return longlats

def long_lat(latlong):  # Converts single LatLong to LongLat
    x = latlong.split(",")
    lat, long = x[0].strip("\n"), x[1].strip("\n")
    longlat = long + "," + lat
    return longlat

def lat_long_for_city_mapper(latlong):  # City Mapper API is annoying and takes a weird latlong format
    x = latlong.split(",")
    lat, long = x[0], x[1]
    Clatlong = lat + "%2C" + long
    return Clatlong

def NoneChecker(variable):
    if variable is None:
        return 0.0
    else:
        return variable






