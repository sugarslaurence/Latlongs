from pprint import pprint as pp
import csv
from Distance import *
from Location import *
from MapboxAPI import *


places = []
location_results = []

def read_file():
    try:
        f = open('/Users/laurencesugars/Documents/Python/latlongs.txt')
        for student in f.readlines():
            places.append(student)
        f.close()
    except Exception:
        print("could not read file")


def save_file(results):
    try:
        f = open("places3.txt", "a")
        for place in results:
            f.write("%s\n" % place)
        f.close()
    except Exception:
        print("could not write to file")


def create_csv(results):
    with open("latlongs.csv", "w") as f:
        w = csv.writer(f)
        w.writerows(results)


def get_location_details(list_of_locations):
    for x in list_of_locations:
        location_one = x
        for x in list_of_locations:
            location_two = x
            result_one = distance_google(location_one, location_two)
            result_two = haversine(location_one, location_two)
            location_results.append(result_one)
            location_results[-1]['Haversine_distance'] = result_two
            google_distance = location_results[-1]["distance"]
            retrieve_distance = distance_calculator()

            haversine_google_diff = retrieve_distance.haversine_google_difference(result_two, google_distance)
            location_results[-1]['Haversine_Google_Diff'] = haversine_google_diff
    return location_results


def haversine(location_one, location_two):  #Invokes Distance_Haversine Function
    result = distance_haversine(location_one, location_two)
    return result

def distance_google(shipFrom, shipTo):  #Retrieves the GoogleAPI distance between two locations
    retrieve_distance = distance_calculator()
    distance = retrieve_distance.get_distance_google(shipFrom, shipTo)
    return distance


def distance_haversine(shipFrom, shipTo):   #Retrieves the Haversine distance between two locations
    retrieve_distance = distance_calculator()
    distance = retrieve_distance.get_distance_haversine(shipFrom, shipTo)
    return distance

def haversine_google_diff(shipFrom, shipTo):    #Retrieves distance difference from two locations between haversine and google API
    retrieve_distance = distance_calculator()
    distance = retrieve_distance.haversine_google_difference(shipFrom, shipTo)
    return distance


def lat_long(shippingAddress):      #Geocoding
    retrieve_latlong = location()
    lat_long = retrieve_latlong.latlong_finder(shippingAddress)
    return lat_long

def address(latLong):       #Reverse Geocoding
    retrieve_address = location()
    address = retrieve_address.address_finder(latLong)
    return address

def optimise(latlongs): #Finds optimal trip between set of latlongs
    retrieve_trip = mapbox()
    longlats = retrieve_trip.long_lats(latlongs)
    trip = retrieve_trip.optimise(longlats)
    print(trip)
    return trip




read_file()
optimise(places)


#get_location_details(places)
#print(pp(location_results))


#save_file(new_list)
#create_csv(new_list)

#latlong = "51.145669, 0.310311"
#print(address(latlong))
#place = "19 Sandhurst Road, TN2 3GA"
#print(lat_long(place))

























