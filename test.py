import requests
from pprint import pprint as pp

waypoints = []


test = "-0.500714,52.142374;-0.076834,51.496301;0.310311,51.145669;-0.077386,51.504136;0.2848889,51.136675"

MAPBOXOPTIMISEAPI = "https://api.mapbox.com/optimized-trips/v1/mapbox/driving/"
key = "pk.eyJ1IjoibGF1cmVuY2VzdWdhcnMiLCJhIjoiY2pjeG5zNzJ5MHQyODM0bnNibHI3dzltYiJ9.tOJ7LUufOlAoQiJ4pIj8Ow"
roundtrip = "roundtrip=true"
access_token = "access_token"

requestURL = "{0}{1}?{2}&{3}={4}".format(MAPBOXOPTIMISEAPI, test, roundtrip, access_token, key)


req = requests.get("https://api.mapbox.com/optimized-trips/v1/mapbox/driving/-0.500714,52.142374;-0.076834,51.496301;0.310311,51.145669;-0.077386,51.504136;0.2848889,51.136675?roundtrip=true&access_token=pk.eyJ1IjoibGF1cmVuY2VzdWdhcnMiLCJhIjoiY2pjeG5zNzJ5MHQyODM0bnNibHI3dzltYiJ9.tOJ7LUufOlAoQiJ4pIj8Ow")
res = req.json()
for waypoint in res:
    waypoints.append(res['waypoints'])

sorted(waypoints[0][0], key = lambda waypoint: waypoint[0][0]["waypoint_index"])
print(waypoints)

#print(type(waypoints))
#print(waypoints[0][0]['waypoint_index'])