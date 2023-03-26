""" 1 есть очередь - потоков клиентов ночного клуба (300) их пропускают барьером по 15 человек
    на столе бочонок пива одновременно налить может только один человек (наливается пиво 1 секунду)
    человек решает хочет или не хочет пива с вероятностью 50 процентов
2 Придумайте сами ситуацию для использования класса таймер      """

import random
from threading import Semaphore, Thread
from time import sleep, time
bar_disco = Semaphore(value=15)

def beer_buyer(number):
    start_service = time()
    with bar_disco:   
        print(f"client {number} started having fun")
        sleep(random.randint(1,5))
        print(f"client {number} service time = {time()-start_service}")
    
buyers = [ Thread(target=beer_buyer, args=(i,)) for i in range(30) ]    
for b in buyers:
    b.start()
from threading import Thread, Event
from time import sleep, time

event = Event()

def runner(name: str):
    event.wait()
    print(f"{name}")
    
runners = [Thread(target=runner, args=(f"runner{i}",)) for i in range(10)]
for d in runners:
    d.start()
    
event.set()