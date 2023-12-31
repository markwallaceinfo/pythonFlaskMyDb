from urllib.error import HTTPError

import requests

try:
    url = 'http://127.0.0.1:5000/stop_server/'
    requests.get(url)
    requests.get('http://127.0.0.1:5001/stop_server/')
except HTTPError as h:
    if h.code == 404:
        print('can not reach site')
    else:
        raise
