# Threads

import threading
import time

def longSquare(num, results):
  time.sleep(1)
  results[num] = num ** 2

results = {}
threads = [threading.Thread(target=longSquare, args=(i, results)) for i in range(0, 5)]
[t.start() for t in threads]
[t.join() for t in threads]


# t1 = threading.Thread(target=longSquare, args=(1, results))
# t2 = threading.Thread(target=longSquare, args=(2, results))

# t1.start()
# t2.start()

# t1.join()
# t2.join()

print(results)

# results = [longSquare(num) for num in range(0, 5)]
# print(results)
