"""
1) генератор(n)
х х х 
х х х
х х х
где х случайное число но таких массивов будет n
сделать список загнать в numpy поменять размерность
2)генератор n случайных колод карт
3)декоратор замеряющий время выполнения функции"""



from pprint import pprint
import random
import time
import numpy
def generator(n, l:list):
    a = numpy.array([
        [random.randint(1,1000) for _ in range(1,4)],
        [random.randint(1,1000) for _ in range(1,4)],
        [random.randint(1,1000) for _ in range(1,4)]])
    n-=1
    l.append(a)
    if n==0:
        return pprint(l)
    return generator(n, l)
generator(6, [])


def coloda():
    nums = [2,3,4,5,6,7,8,9,10,"Валет", "Дама", "Король", "Туз"]
    kinds = ["Пики","Буби", "Крести", "Череви"]
    for x in kinds:
        for y in nums:
            yield(x,y)


def dtime():  
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            return print(f"Finished Time {time.perf_counter()-start}")
        return wrapper
    return decorator
@dtime()
def generatorrandomcoloda(n):
    l = list(coloda())
    rlist = []
    for x in range(len(l)-1, -1, -1):
        k = random.randint(0,x)
        rlist.append(l.pop(k))
    n-=1
    if n == 0:
        return     
    return generatorrandomcoloda(n) 

generatorrandomcoloda(5) 