import numpy as np
import time
from smooth_alternative import smooth
from smooth_alternative import smooth_numpy
from smooth_alternative import smooth_numpy_alt
from smooth_alternative import smooth_alt

x =  [float(i) for i in np.random.randn(100000,1)]
h = 2000


print("Smooth: ")
start = time.time()
z = smooth(x,h)
elapse = time.time() - start
print(elapse)


print("smooth_numpy: ")
start = time.time()
z1 = smooth_numpy(x,h)
elapse = time.time() - start
print(elapse)


print("smooth_numpy_alt: ")
start = time.time()
z2 = smooth_numpy_alt(x,h)
elapse = time.time() - start
print(elapse)


print("smooth_alt: ")
start = time.time()
z3 = smooth_alt(x,h)
elapse = time.time() - start
print(elapse)

