import numpy as np
def sm(x):
    s = 0
    for i in range(0, len(x)):
                 s = s+x[i]
    return s

x = np.arange(0,10)
y = sm(x)
print(x)
print(y)


