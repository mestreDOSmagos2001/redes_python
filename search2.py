import requests
from pprint import pprint
address = input('Digite seu endereço para saber sua localizaçao em lat lon: ')
url = f'https://nominatim.openstreetmap.org/?format=json&addressdetails=1&q={address}'
req = requests.get(url).json()
pprint(f"Latitude = {req[0]['lat']}, longitude = {req[0]['lon']}")
