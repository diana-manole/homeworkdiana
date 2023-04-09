""" генератор(n)
х х х 
х х х
х х х
где х случайное число но таких массивов будет n """

from pprint import pprint
import numpy
import random
    
def generator(n, l:list):
    for x in l:
        for _ in range(n):
            yield x

a = numpy.array([
        [random.randint(1,1000) for _ in range(1,4)],
        [random.randint(1,1000) for _ in range(1,4)],
        [random.randint(1,1000) for _ in range(1,4)]])

for x in generator( 1,a):
    print(x)

