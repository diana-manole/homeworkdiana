""" from threading import Thread
from time import sleep

def func(number):
    print(f"I am func number {number}! ")
    sleep(3.4)
   
l = [ Thread(target=func, args=(x,)) for x in range(1,100) ]
for t in l :
    t.start()
for t in l :
    t.join()

l1 = [ Thread(target=func, args=(x,)) for x in range(101,200) ]
for t in l1 :
    t.start()
for t in l1 :
    t.join()
    
l2 = [ Thread(target=func, args=(x,)) for x in range(201,300) ]
for t in l2 :
    t.start()
for t in l2 :
    t.join()
     """
from random import randint
numbers=[]        
l=[randint(1,1_000_000) for i in range(0, 1_000_000)]

print(l)

""" 
with open("advs.txt",encoding="utf-8") as f:
    fulltext = f.read()
    fulltext =''.join ([x for x in fulltext if x.isalpha() or x == ' ']) 
    fulltext = fulltext.lower()
    ls = fulltext.split()

print(fulltext) """
