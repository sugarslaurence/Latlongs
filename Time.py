import requests
from ApiKeys import *
from URLs import *
from datetime import datetime
from Functions import *
import googlemaps

class time_calculator:

    def get_time_mapbox(self, shipFrom, shipTo):    # Retrieves a time matrix between two locations from Mapbox
        access_token = "access_token"
        key = key_mapbox_default
        URL = MAP_BOX_DISTANCE_URL
        requestURL = "{0}{1};{2}?{3}={4}".format(URL,shipTo,shipFrom,access_token,key)
        req = requests.get(requestURL)
        res = req.json()    # Res is a dict
        durationFromTo = res['durations'][0][1]
        durationToFrom = res['durations'][1][1]

        if durationFromTo != durationToFrom:
            if durationFromTo > durationToFrom:
                return durationFromTo
            else:
                return durationToFrom


    def get_time_city_mapper(self, shipFrom, shipTo):   # Retrieves the time, based on the current date time, from City Mapper
        URL = "https://developer.citymapper.com/api/1/traveltime/?"
        key = key_city_mapper
        time = datetime.now()
        requestURL = "{0}startcoord={1}&endcoord={2}&time={3}&timetype=arrival&key={4}".format(URL, shipFrom, shipTo, time, key)
        req = requests.get(requestURL)
        res = req.json()
        duration = res['travel_time_minutes']
        return duration


    def get_duration_google(self, shipFrom, shipTo):    # Retrieves duration between two points from Google
        gmaps = googlemaps.Client(key_distance)
        my_distance = gmaps.distance_matrix(shipFrom, shipTo)
        rows = my_distance["rows"][0]["elements"][0]
        duration = rows["duration"]["value"]
        return duration

    def get_duration_graph_hopper(self, shipFrom, shipTo):
        duration = graph_hopper()
        graph_hopper_routing = duration.graph_hopper_routing(shipFrom, shipTo)
        graph_hopper_duration = graph_hopper_routing['time']
        return graph_hopper_duration