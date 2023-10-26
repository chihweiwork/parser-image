import requests
from pprint import pprint

url = 'http://127.0.0.1:8000/imageParser'
#files = [('files', open('images/1.png', 'rb')), ('files', open('images/2.png', 'rb'))]
#files = [('files', open('./test.png', 'rb'))]
file = {'file': open('./test.png', 'rb')}
resp = requests.post(url=url, files=file) 
#pprint(resp.json())
print(resp.json())
