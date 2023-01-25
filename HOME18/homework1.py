'https://www.google.com/search?client=safari&rls=en&q=free+api+for+testing+without+key&ie=UTF-8&oe=UTF-8'


#выберите и сделайте обращания к api

from superclassapi import GetFromApi
from pprint import pprint

import requests
'''
res = requests.get('https://scotch.io')
print(res)
print(res.headers)
'''
response = requests.get("https://randomuser.me/api/")
pprint(response.text)



