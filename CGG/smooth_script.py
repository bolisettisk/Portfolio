import numpy as np
import time
from smooth import smooth

  
x =  [float(i) for i in np.random.randn(10000,1)]
h = 2000

x = np.arange(0,5)
h = 2

print("Smooth: ")
start = time.time()
z = smooth(x,h)
elapse = time.time() - start
print(elapse)
print(x)
print(z)
