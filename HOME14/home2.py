"""1 база доходов компании - в классе финанс есть поле резалтс 
график - три линии - три бизнеса
ось икс - это год и месяц
ось игрек - это доход
три линии для трех бизнесов

2 попробуйте сделать три разных графика чтобы были не линии а столбики на разных окошках

3 котики
ось икс - выставки
ось игрек - участники"""

import mysql.connector 
from itertools import groupby
import matplotlib.pyplot as plt

finddb = mysql.connector.connect(
    host='localhost',
    user='python',
    password='!QA2ws3ed=-2'
)
cursor = finddb.cursor()
query ='SELECT * FROM study.exhibit LEFT JOIN study.cat_exhibit_relation ON  exhibit.idexhibit = cat_exhibit_relation.exhibitid LEFT JOIN study.cats ON  cats.id = cat_exhibit_relation.catid  '

cursor.execute(query)
results = cursor.fetchall()
print(results)


x=list(map(lambda y:str(y[1]),results))
y =list(map(lambda y:str(y[5]),results))

plt.style.use("bmh")
fig, axs = plt.subplots()
axs.scatter(x,y, linewidth=5)
plt.show()