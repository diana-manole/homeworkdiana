"""
5 напишите сравнение двух серий (числовых)"""

import pandas as pd
from pprint import pprint

s1 = pd.Series([1,3,5,7,9,11,13,15])
s2 = pd.Series([1,2,3,4,5,6,7,8])

ms = pd.Series(s2, index=s1)
pprint(ms)

ser = pd.Series(range(8), index=[1,3,5,7,9,11,13,15])
print(ser)

