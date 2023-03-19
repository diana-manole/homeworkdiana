from threading import Thread
from time import sleep, perf_counter

import concurrent.futures

def waiter(n):
    print(f'thread started {n}')
    sleep(3)
    print(f'thread ended  {n} ')
    
start_time = perf_counter()    

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(waiter, range(3))
print('done')


end_time = perf_counter()

print(f'Time taken: {end_time-start_time: 0.2f} seconds')