import requests

GOOGLE_MAPS_API_URL = 'http://maps.googleapis.com/maps/api/geocode/json'

params = {
    'latlng' : "51.145669, 0.310311",
    'sensor' : 'false',
    'region' : 'uk'

}

#params = {
#    'address': '105 Corio House, Bermondsey, London',
#    'sensor': 'false',
#    'region': 'uk'
#}

req = requests.get(GOOGLE_MAPS_API_URL, params=params)
res = req.json()
print(res)

result = res['results'][0]
geodata = dict()
geodata['lat'] = result['geometry']['location']['lat']
geodata['lng'] = result['geometry']['location']['lng']
geodata['address'] = result['formatted_address']

print('{address}. (lat, lng) = ({lat}, {lng})'.format(**geodata))
print('{lat},{lng}'.format(**geodata))