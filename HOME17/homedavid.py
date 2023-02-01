import plotly.express as px
import flet as ft
import pandas
from flet.plotly_chart import PlotlyChart
from superclass import GetFromApi
from itertools import groupby

url = "https://datausa.io/api"
method = "data"
parameters = {"drilldowns": "State", "measures": "Population"}

l = (
    GetFromApi(url)
    .addMethod(method=method, parameters=parameters)
    .GetDataFromApi()
    .GetValueFromKey("data")
)
# sorted(l,key=lambda x: (x[2],x[0]))
# print(l)
# del l()
w = dict(
    map(
        lambda t: (t[0], dict(map(lambda g: (g["State"], g["Population"]), t[1]))),
        groupby(l, lambda x: x["Year"]),
    )
)

group = pandas.DataFrame(w)

print(group)

x = []
y = []
for pair in w["2013"]:
    x.append(pair[0])
    y.append(pair[1])


def main(page: ft.Page):

    fig = px.bar(group, height=400)
    page.add(PlotlyChart(fig, expand=True))


ft.app(target=main)
