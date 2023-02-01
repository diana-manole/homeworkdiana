import requests
from itertools import groupby
from superclassapi import GetFromApi

url = "https://developer.shopgate.com/"

headers = {"Accept": "application/json"}

r = requests.get(url=url, headers=headers)
# print(r)
# /////////////////////

url = "https://api.zippopotam.us/us/33162"

headers = {"Accept": "application/json"}

r = requests.get(url=url, headers=headers)

zip = list(r.json())
# print(zip)
# /////////////////////

url = "https://ipinfo.io/161.185.160.93/geo"
method = "data"
params = {
    "ip": "161.185.160.93",
    "city": "New York City",
    "region": "New York",
    "country": "US",
    "loc": "40.7143,-74.0060",
    "org": "AS22252 The City of New York",
    "postal": "10004",
    "timezone": "America/New_York",
    "readme": "https://ipinfo.io/missingauth",
}


l = (
    GetFromApi(baseURL=url)
    .addMethod(method=method, parameters=params)
    .GetDataFromApi()
    .GetValueFromKey("data")
)
print(l)
