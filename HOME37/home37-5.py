""" 3 сделайте numpy array - сконвертируйте в серию """

import pandas as pd
from pprint import pprint
import numpy as np


df = pd.DataFrame( np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [7, 8, 9]]),[1,2,3,4])
pprint(df)
