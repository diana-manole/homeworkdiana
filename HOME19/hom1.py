"""1 разобраться ПОЛНОСТЬЮ с кодом
https://habr.com/ru/post/346306/
2 создать и предоставить все git  с ДЗ
3 продумать как можно использовать диапазоны - нпример год с 2019 по 2021 ???
4 воплотить в жизнь"""


from day19_api1 import incomes
from itertools import groupby
import mysql.connector
from dbFile import DataHelp

d = DataHelp()
query = "select year, month, business.name as business, income from Predicator.Finances left join Predicator.business on business.id=business"
r = d.executeSomeQuery(query=query)
print(r)
