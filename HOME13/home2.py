from tensorflow import *
from keras import *
from keras import layers

model=Sequential()

model.add(layers.Dense(units=12,input_shape=[1]))

model.add(layers.Dense(units=8,input_shape=[1]))

model.add(layers.Dense(units=1,input_shape=[1]))
input_list = [1, 2, 3, 4, 5, 6, 7, 8]
output_list = [1, 4, 9, 16, 25, 36, 49, 64]

model.compile(loss='mean_squared_error',optimizer='adam')

model.fit(x=input_list,y=output_list,epochs=1000)

model.save('tensor1')
model = models.load_model('tensor1')
print(model.predict([9]))
print(model.predict([10]))
print(model.predict([11]))
print(model.predict([12]))
print(model.predict([13]))