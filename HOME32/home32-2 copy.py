
""" 2 Создайте класс котоый будет генерировать массив из 10_000_000 случайных чисел и писать в файл имя которого вы предложите
запустите три таких потока 
 """
from threading import Thread
from time import sleep
from random import randint

def func(number):
    print(f"I am func number {number}! ")
    sleep(3.4)

numbers=[] 
for i in range(0, 1_000_000):      
   numbers.append(randint(0, 1_000_000))
   
numbers1=[] 
for i in range(0, 1_000_000):      
   numbers1.append(randint(0, 1_000_000))
   
numbers2=[] 
for i in range(0, 1_000_000):      
   numbers2.append(randint(0, 1_000_000))

l = [ Thread(target=func, args=(x,)) for x in numbers ]
for t in l :
    t.start()
for t in l :
    t.join()

l2 = [ Thread(target=func, args=(x,)) for x in numbers1 ]
for t in l :
    t.start()
for t in l :
    t.join()
    
l2 = [ Thread(target=func, args=(x,)) for x in numbers2 ]
for t in l :
    t.start()
for t in l :
    t.join()