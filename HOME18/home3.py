import requests
import pprint
url = 'https://httpbin.org/get'
headers = {'Content-Type': 'text/html'}

response = requests.get('https://httpbin.org/get')
print(response.headers)



