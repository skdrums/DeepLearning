import numpy as np

x=np.random.randint(0,10,(8,10))

print(x)
print(x.mean())

print(x.var())

print(x.std())

print(x.max())

print(x.min())

print(x.mean(axis=1)) #ある次元（axis)におけるそれぞれの平均
# 上と下は等価
print(np.array([
    x[0, :].mean(),
    x[1, :].mean(),
    x[2, :].mean(),
    x[3, :].mean(),
    x[4, :].mean(),
    x[5, :].mean(),
    x[6, :].mean(),
    x[7, :].mean(),
]))

