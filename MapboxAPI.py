from ApiKeys import *
import requests

MAPBOXOPTIMISEAPI = "https://api.mapbox.com/optimized-trips/v1/mapbox/driving/"


waypoints = []

class mapbox:

    def long_lats(self, latlongs):
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

    def optimise(self, longlats):

        roundtrip = "roundtrip=true"
        access_token = "access_token"
        key = key_mapbox_default
        requestURL = "{0}{1}?{2}&{3}={4}".format(MAPBOXOPTIMISEAPI, longlats, roundtrip, access_token, key)

        req = requests.get(requestURL)
        res = req.json()

        return res




