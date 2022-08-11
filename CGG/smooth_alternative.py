import numpy as np
""" Diffferent versions of the smooth function """

def smooth(inlist, h):
    outlist = list()
    N = len(inlist)
    k1 = set(list(range(0,N)))
    for i in range(0,N):
        k = k1 & set(range(i-h, i+h+1))
        outlist.append(sum([inlist[i] for i in k])/len(k))
    return outlist


def smooth_numpy(inlist, h):
    outlist = list()
    N = len(inlist)
    k1 = set(np.arange(0,N))
    for i in range(0,N):
        k = k1 & set(np.arange(i-h, i+h+1))
        outlist.append(np.mean([inlist[i] for i in k]))
    return outlist


def smooth_numpy_alt(inlist, h):
    outlist = list()
    N = len(inlist)
    k1 = set(np.arange(0,N))
    for i in range(0,N):
        k = set.intersection(k1, set(np.arange(i-h, i+h+1)))
        outlist.append(np.mean([inlist[i] for i in k]))
    return outlist


def smooth_alt(inlist, h):
    outlist = list()
    N = len(inlist)
    k1 = set(list(range(0,N)))
    for i in range(0,N):
        k = set.intersection(k1, set(range(i-h, i+h+1)))
        outlist.append(sum([inlist[i] for i in k])/len(k))
    return outlist
