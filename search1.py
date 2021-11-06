import ssl
import certifi
from geopy.geocoders import Nominatim
import geopy
ctx = ssl.create_default_context(cafile=certifi.where())
geopy.geocoders.options.default_ssl_context = ctx
address = input('Digite Seu endereço para saber as coordenadas: ')
user_agent = 'Foundations of Python Network Programming example search1.py'
location = Nominatim(user_agent=user_agent).geocode(address)
print(f'Sua latitude é {location.latitude} e sua longitude é {location.longitude}')
