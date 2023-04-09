""" 2 есть словарь {'a':100, 'b':200, 'c':300, 'd':400}
    конвертировать в серию
 """
from pprint import pprint
import pandas as pd

df = pd.DataFrame({'a':[100], 'b':[200], 'c':[300], 'd':[400]})
pprint(df)

mydict = {"a":100, 'b': 200, 'c': 300, 'd':400}
ms = pd.Series(mydict)
pprint(ms)