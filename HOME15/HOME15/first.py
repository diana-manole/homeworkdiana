import mysql.connector
from itertools import groupby
import matplotlib.pyplot as plt


finddb = mysql.connector.connect(
    host="localhost", user="python", password="!QA2ws3ed=-2"
)
cursor = finddb.cursor()
query = "SELECT (business),(income) FROM predicator.finances "
cursor.execute(query)
results = cursor.fetchall()
# print(results)

d = dict(
    map(
        lambda y: (y[0], list(map(lambda x: (x[0:]), y[1]))),
        groupby(results, key=lambda x: x[0]),
    )
)
print(d)

# print("////////////////////////////////////")

cursor1 = finddb.cursor()
query1 = "SELECT(year),(month) FROM predicator.finances "
cursor1.execute(query1)
results1 = cursor.fetchall()
# print(results1)


x = list(map(lambda y: str(y[0]) + "/" + str(y[1]), results1))
y = list(map(lambda y: str(y[1]), results))
y1 = list(map(lambda y: str(y[1]), results))
y2 = list(map(lambda y: str(y[1]), results))

fig, axs = plt.subplots()

"""
axs.bar(x1,y)
axs.bar(x1,y1)
axs.bar(x1,y2)"""

axs.plot(x, y)
axs.plot(x, y1)
axs.plot(x, y2)
# plt.show()
