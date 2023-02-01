d = {
    "ID State": "04000US01",
    "State": "Alabama",
    "ID Year": 2018,
    "Year": "2018",
    "Population": 4864680,
    "Slug State": "alabama",
}
# print(d)
# print(d['State'])

d1 = [
    {
        "ID State": "04000US01",
        "State": "Alabama",
        "ID Year": 2018,
        "Year": "2018",
        "Population": 4864680,
        "Slug State": "alabama",
    },
    {
        "ID State": "04000US02",
        "State": "Alaska",
        "ID Year": 2018,
        "Year": "2018",
        "Population": 738516,
        "Slug State": "alaska",
    },
    {
        "ID State": "04000US04",
        "State": "Arizona",
        "ID Year": 2018,
        "Year": "2018",
        "Population": 6946685,
        "Slug State": "arizona",
    },
    {
        "ID State": "04000US05",
        "State": "Arkansas",
        "ID Year": 2018,
        "Year": "2018",
        "Population": 2990671,
        "Slug State": "arkansas",
    },
    {
        "ID State": "04000US06",
        "State": "California",
        "ID Year": 2018,
        "Year": "2018",
        "Population": 39148760,
        "Slug State": "california",
    },
    {
        "ID State": "04000US08",
        "State": "Colorado",
        "ID Year": 2018,
        "Year": "2018",
        "Population": 5531141,
        "Slug State": "colorado",
    },
]

print(d1[3])
# print(d1.index('State'))

# print(list(filter(lambda x:x['State']==['Alabama'],d1)))
# print(d1,[0],[1])
# d1.sort(key="State")
# d1.values()
# print(sorted(d1.items()))

# i=dict()
# x=[i for i in list(l) if i==l[3] ]
# print(x)
"""
d = dict(
    map(
        lambda y: (y[0], list(y[1])),
        groupby(l, key=lambda x: x[0])
    )
)
print(d)"""

# x=map(lambda x:x=='State',l)
# x= list( filter( lambda x: x[3] == x[3],l))
