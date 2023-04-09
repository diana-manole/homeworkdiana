""" 4 сконвертировать серии списков в одну серию
 0 [red, Green, White]
 1 [red, black]
 2 [yellow]
 """
import pandas as pd
from pprint import pprint

""" s = pd.Series([
    ['Red', 'Green', 'White'],
    ['Red', 'Black'],
    ['Yellow']])
unique=[]
for x in s:
    if x not in unique:
        unique.append(x) 
print(unique)
df = pd.DataFrame(unique)
pprint(df)
 """

import pandas as pd
s = pd.Series([
    ['Red', 'Green', 'White'],
    ['Red', 'Black'],
    ['Yellow']])

s = s.apply(pd.Series).stack().reset_index(drop=True)
print(s)
