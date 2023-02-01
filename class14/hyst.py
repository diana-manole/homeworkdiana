from plotly.graph_objs import Bar, Layout
import matplotlib.pyplot as plt
import seaborn as sn
import numpy as np

years = [1998, 1999, 2000, 2001, 2002, 2003, 2004]
incomes = [1000000, 1500000, 1700000, 2300000, 2800000, 3200000, 4500000]
fig, axs = plt.subplots(1, 1)
# data=[Bar(X=years,Y=incomes)]
# axs[0].hist(years,bins=20)
# axs.hist(np.array(incomes),bins=years )
axs.bar(years, height=incomes)
plt.show()
