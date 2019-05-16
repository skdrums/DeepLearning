import numpy as np

a=np.array([
    [0,1,2,1,0],
    [3,4,5,4,3],
    [6,7,8,7,6],
    [3,4,5,4,4],
    [0,1,2,1,0]
])
b=np.array([1,2,3,4,5])

c = np.empty((5,5))
for i in range(a.shape[0]): # a.shape[0] 行数
    c[i,:]=a[i,:]+b
d = np.empty((5,5))
d= a+b
print(c)
print(d)