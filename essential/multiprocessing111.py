# Processes
from multiprocessing import Process
import time

def longSquare(num):
  time.sleep(1)
  print(num ** 2)
  print(f"Process {num} finished")

processes = [Process(target=longSquare, args=(i,)) for i in range(0, 5)]
[p.start() for p in processes]
[p.join() for p in processes]


