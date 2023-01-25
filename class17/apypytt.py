'''import requests
from itertools import groupby

url="http://universities.hipolabs.com/search"
#?country=United+States"

headers = {'Accept': 'application/json'}

r=requests.get(url=url,headers=headers)

universities=list(r.json())
countries=list(map(lambda x: x['country'],universities))
countries.sort()
countries=list(map(lambda t:t[0],groupby(countries, lambda x: x)))

print(countries)/'''
import requests
from itertools import groupby

url="http://universities.hipolabs.com/search"
#?country=United+States"

headers = {'Accept': 'application/json'}

r=requests.get(url=url,headers=headers)

universities=list(r.json())
countries=list(map(lambda x: x['country'],universities))
countries.sort()
countries=list(map(lambda t:t[0],groupby(countries, lambda x: x)))

print(countries)