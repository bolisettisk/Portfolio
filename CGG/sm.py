import numpy as np

def sm(x):
    s = 0
    for i in range(0, len(x)):
                 s = s+x[i]
    return s


def sm_alt(x):
    s = 0
    for i in x:
                 s = s+i
    return s

def sum_1(x):
    return np.sum(x)
    
    





