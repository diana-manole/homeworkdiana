""" 4 сделайте список в в три потока заполните его числами 1 - 1 - 1_000_000 2 - 1_000_001 - 2_000_000 3 2_000_001 - 3_000_000
каждый поток генерит список чисел а потом вы берете списко основного кода или основного потока приложения
используйте lock"""
from threading import Thread,Lock
from time import sleep

lock = Lock()
stop_thread = False

def func(number,f):
    while True:
        print(f"I am number {number}!,поток{f} ")
        if lock.acquire(blocking = True, timeout=1):
            if stop_thread is True:
                lock.release()
                break
            lock.release()
        sleep(0.5)

l = [ Thread(target=func, args=(x,1,)) for x in range(1,100) ]
l1 = [ Thread(target=func, args=(x,2,)) for x in range(101,200) ]    
l2 = [ Thread(target=func, args=(x,3,)) for x in range(201,300) ]

list=[]

for i in l:
    list.append(i)
for i in l1:
    list.append(i)
for i in l2:
    list.append(i)

for t in list :
    t.start()
  
sleep(2)

lock.acquire()
stop_thread = True
print("Stop threads!")
sleep(3)
lock.release()