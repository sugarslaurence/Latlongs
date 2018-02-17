from ApiKeys import *
import requests
from operator import itemgetter
from pprint import pprint as pp
from URLs import *

waypoints = []

class optimise:

    def map_box_optimise(self, longlats):

        roundtrip = "roundtrip=true"
        access_token = "access_token"
        key = key_mapbox_default
        URL = MAP_BOX_OPTIMISE_API
        requestURL = "{0}{1}?{2}&{3}={4}".format(URL, longlats, roundtrip, access_token, key)

        req = requests.get(requestURL)
        res = req.json()

        waypoints.append(res['waypoints'])
        waypointslist = waypoints[0]

        sortedwaypoints = sorted(waypointslist, key=itemgetter('waypoint_index'))

        return sortedwaypoints

    def graph_hopper_optimise(self, locations):
        pass







