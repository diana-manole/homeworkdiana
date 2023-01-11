import matplotlib.pyplot as plot
"""
x= list(range(1,1001))
y= list(map(lambda y:y**2,x))

fig, axs =plot.subplots()
axs.scatter(x,y,c =y,cmap=plot.cm.Blues,s=5)
plot.show()"""
import matplotlib.pyplot as plt
import math
"""
x= list(range(-100,101))
y= [math.sqrt(100**2-t**2) for t in x]
#y1= [-math.sqrt(100**2-t**2) for t in x]
fig, axs =plt.subplots()
axs.plot(x,y,c="pink")
#axs.plot(x,y1)
plt.show()
"""
x=[
    (2002,1,1),
    (2002,2,1),
    (2002,3,1),
    (2002,4,1)
]

x1=list(map(lambda y:str(y[0])+"/"+str(y[1]),x))
y=[1200,900,1300,1400]
y1=[100,1900,2300,2400]
y2=[200,800,1200,1500]

fig,axs =plt.subplots()
"""
axs.bar(x1,y)
axs.bar(x1,y1)
axs.bar(x1,y2)"""
axs.plot(x1,y)
axs.plot(x1,y1)
axs.plot(x1,y2)
plt.show()
