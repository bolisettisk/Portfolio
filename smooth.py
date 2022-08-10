import numpy as np
def smooth(inlist, h):
    import numpy as np
    outlist = list()
    N = len(inlist)
    k1 = set(np.arange(0,N))
    for i in range(0,N):
        k = k1 & set(np.arange(i-h, i+h+1))
        #k = k1 & k2
        outlist.append(np.mean([inlist[i] for i in k]))
    return outlist
                  
     
y = np.random.randn(100000,1)
#y = np.arange(0,10)
x =  [float(i) for i in y]
z = smooth(x,2)
print(x)
print(z)


