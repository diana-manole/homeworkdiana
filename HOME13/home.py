#создаете массив для теста и проверок например числа фибоначчи и тренируете нейросеть для предсказания
from tensorflow import *
from keras import *
from keras import layers
"""
#a^2+b^2=c^2
#input=[1^2+2^2,2^2+3^2,3^2+4^2,4^2+5^2,5^2+6^2]
#input=[(1^2),(2^2),(3^2),(4^2),(5^2)]
input=[1,2,3,4,5,6,7,8,9]
output=[1,4,9,16,15,36,49,64,81]
#creating neural network
model = models.Sequential()
#input layer
model.add(layers.Dense(units=5,input_shape=[1]))
#intermediate layer 
model.add(layers.Dense(units=2000,input_shape=[1]))
model.add(layers.Dense(units=1800,input_shape=[1]))
model.add(layers.Dense(units=320,input_shape=[1]))
model.add(layers.Dense(units=1,input_shape=[1]))

model.compile(optimizer="adam",loss="mean_squared_error")

model.fit(x=input,y=output,epochs=800)

print(model.predict([10]))
"""
from functools import reduce
def redo(x,y):
    return x*y

l = [1,2,3,4,5]
r = reduce(redo, l)
print(r)
# [1+2]  = 3 . [1*2]  = 2
# [3+3]  = 6 . [2*3]  = 6
# [6+4]  = 10  [6*4]  = 24
# [10+5] = 15  [24*5] = 120
"""
input=[1,2,3,4,5,6]
output=[1,4,9,14,25,36]
model = models.Sequential()
model.add(layers.Dense(units=50,input_shape=[1]))
model.add(layers.Dense(units=200,input_shape=[1]))
model.add(layers.Dense(units=1800,input_shape=[1]))
model.add(layers.Dense(units=320,input_shape=[1]))

model.add(layers.Dense(units=1,input_shape=[1]))
model.compile(optimizer="adam",loss="mean_squared_error")

model.fit(x=input,y=output,epochs=500)

print(model.predict([7]))
"""