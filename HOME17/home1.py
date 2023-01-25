'''РАзобраться с методом работы с АПИ
получить по апи статистику и вывести как диаграмму за определенный год население штатов как столбики'''
from superclass import GetFromApi
from itertools import groupby
import matplotlib.pyplot as plt
import pandas
# https://datausa.io/api/data?drilldowns=Nation&measures=Population

url = 'https://datausa.io/api/'
method = 'data'

params = {'drilldowns': 'State', 'measures': 'Population', "year": "2019"}
l = GetFromApi(baseURL=url).addMethod(
    method=method, parameters=params).GetDataFromApi().GetValueFromKey("data")
print(l)


d = [{k:d[k] for k in d if k in ["Population","State","Year"]} for d in l]

#print(d.keys)
#print(list(n for n in d if key='State'))

#print(d)

"""
state =[]
for x in d:
    state.append(x["State"])

poplation =[]
for y in d:
    poplation.append(y["Population"])

group = pandas.DataFrame(d)

fig, axs = plt.subplots(1,1)
axs.bar(state, height= poplation)
plt.xticks(state, rotation=90)
plt.show()
"""


