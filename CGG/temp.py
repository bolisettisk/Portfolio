import numpy as np

x =  [float(i) for i in np.random.randn(1000,1)]
N = len(x)

h = 200
i = 900
k1_smooth = set(np.arange(0,N))
k1_smooth_2 = set(list(range(0,N)))

k_smooth = k1_smooth & set(np.arange(i-h, i+h+1))
k_smooth_2 = k1_smooth_2 & set(list(range(i-h, i+h+1)))

xi_smooth = [x[i] for i in k_smooth]
mean_smooth = np.mean(xi_smooth)
xi_smooth_2 = [x[i] for i in k_smooth_2]
mean_smooth_2 = sum(xi_smooth_2)/len(k_smooth_2)

print(k_smooth)
print(k_smooth_2)
print("-------------------------------------------------------")
print(xi_smooth)
print(xi_smooth_2)
print("-------------------------------------------------------")
print(mean_smooth)
print(mean_smooth_2)
print(sum(xi_smooth)/len(k_smooth))
print("-------------------------------------------------------")
print(np.array(xi_smooth)-np.array(xi_smooth_2))
print("-------------------------------------------------------")
print(len(k_smooth))
print(len(k_smooth_2))
