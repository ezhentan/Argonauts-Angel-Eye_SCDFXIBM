import json
import urllib
from urllib.parse import urlparse

import httplib2 as http

#Authentication 
headers = {'AccountKey': 'Snr9UB/rQZC1s1ApQD+TlA==',  # this is my API key
               'accept': 'application/json'}
    
#API Parameters
url = 'http://datamall2.mytransport.sg/'
path = 'ltaodataservice/Traffic-Imagesv2'  # this changes according to the different APIs you want, the links are in the documentation

#Build query string & specify type of API call
target = urlparse(url + path)
print(target.geturl())
method = 'GET'
body = ''

h = http.Http()

response, content = h.request(
    target.geturl(),
    method,
    body,
    headers)
    
#Parse JSON to print     
jsonObj = json.loads(content)
print(json.dumps(jsonObj, sort_keys=True, indent=4))
