import numpy as np
def smooth(inlist, h):
    """  This function performs a basic smoothing

            of inlist and returns the result (outlist).

            Both lists have the same length, N.  Each

            item in inlist should have type 'float' and

            'h' should be an integer.  For each i,

            outlist[i] will be the average of inlist[k]

            over all k that satisfy  i-h <= k <= i+h

            and  0 <= k <= N-1.  """
    outlist = list()
    N = len(inlist)
    k1 = set(list(range(0,N)))
    for i in range(0,N):
        k = set.intersection(k1, set(range(i-h, i+h+1)))
        outlist.append(sum([inlist[i] for i in k])/len(k))
    return outlist
