import requests
from pprint import pprint

url = 'http://127.0.0.1:8000/imageParser' # API
file = {'file': open('./test.png', 'rb')} # open image file
resp = requests.post(url=url, files=file) # post information to api server 
print(resp.json())                        # get response
