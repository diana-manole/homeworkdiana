from threading import Thread
from time import sleep, perf_counter

def waiter(n):
    print(f'thread {n} started ')
    sleep(3)
    print(f'thread {n} ended  ')
    
start_time = perf_counter()

threads = []

for n in range(1,11):  
    th = Thread(target=waiter, args=(n,))
    threads.append(th)
    th.start()
    
  
end_time = perf_counter()

print(f'Time taken: {end_time-start_time: 0.2f} seconds')


