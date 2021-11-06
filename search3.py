import http.client
import json
from urllib.parse import quote_plus
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


address = input('Digite o endereçco: ')
path = f'/?format=json&addressdetails=1&q={quote_plus(address)}'
user_agent = b'search3.py'
headers = {b'User-Agent': user_agent}
con = http.client.HTTPSConnection('nominatim.openstreetmap.org')
con.request('GET', path, None, headers)
res_bruta = con.getresponse().read()
res_tratada = json.loads(res_bruta.decode('utf-8'))
print(f"Latitude = {res_tratada[0]['lat']}, longitude = {res_tratada[0]['lon']}")
