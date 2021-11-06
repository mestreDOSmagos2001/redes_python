import socket
from urllib.parse import quote_plus
from pprint import pprint
import ssl

request_text = """\
GET /?format=json&addressdetails=1&q={}\r\n\
HTTP/1.1\r\n\
HOST: nominatim.openstreetmap.org\r\n\
User-Agent: search4.py\r\n\
Connection: close\r\n\
\r\n\
"""
def geocode(address):
    unencrypted_sock = socket.socket()
    unencrypted_sock.connect(('nominatim.openstreetmap.org', 443))
    sock = ssl.wrap_socket(unencrypted_sock)
    request = request_text.format(quote_plus(address))
    sock.sendall(request.encode('ascii'))
    raw_replay = b''
    while True:
        more = sock.recv(4096)
        if not more:
            break
        raw_replay += more
    pprint(raw_replay.decode('utf-8'))


geocode('jardim bangu')
