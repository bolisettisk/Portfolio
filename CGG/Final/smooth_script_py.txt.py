import numpy as np
import time
from smooth import smooth

  
x =  [float(i) for i in np.random.randn(10000,1)]
h = 2000


print("Smooth: ")
start = time.time()
z = smooth(x,h)
elapse = time.time() - start
print(elapse)

