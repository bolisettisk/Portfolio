import numpy as np
import pandas as pd
from numpy.random import randn
from sm import sm
from sm import sm_alt
from sm import sum_1

x = randn()
print(x)
print(type(x))
print("-------------------------------------------------------------")
print("-------------------------------------------------------------")

a = randn(10,1)
print(a)
print("-------------------------------------------------------------")
print("-------------------------------------------------------------")

b = sm_alt(a)
print(b)
print("-------------------------------------------------------------")
print("-------------------------------------------------------------")

c = sum_1(a)
print(c)

