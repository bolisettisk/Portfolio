import numpy as np

N = 100
a = np.arange(0,N)
b = np.arange(10,N-10)

import time
start = time.time()
for _ in range(1000):
    result = [x for x in a if x in b]
elapse = time.time() - start
print(elapse)
print(result)


c = set(a)
start = time.time()
for _ in range(1000):
    result = c & set(b)
elapse = time.time() - start
print(elapse)
print(result)

start = time.time()
for _ in range(1000):
    result = set.intersection(set(a), set(b))
elapse = time.time() - start
print(elapse)
print(result)

start = time.time()
for _ in range(1000):
    result = set.intersection(c, set(b))
elapse = time.time() - start
print(elapse)
print(result)

start = time.time()
for _ in range(1000):
    result = np.intersect1d(a, b)
elapse = time.time() - start
print(elapse)
print(result)



