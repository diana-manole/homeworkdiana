
""" 2 Создайте класс котоый будет генерировать массив из 10_000_000 случайных чисел и писать в файл имя которого вы предложите
запустите три таких потока 
 """
from threading import Thread
from time import sleep
from random import randint

class count(Thread):
    def __init__(self,numbers):
        Thread.__init__(self)
        self._numbers = numbers
    
    def func(self) -> None:
        for i in range(self._limit):
            print(f'number {i}')
            sleep(0.5)

numbers=[] 
for i in range(0, 1_000_000):      
   numbers.append(randint(0, 1_000_000))
"""randint(count(0,1000)for i in range(1000)) """
mythread =count(numbers=[randint((0,1000) for i in range(1000))])
mythread.start()
