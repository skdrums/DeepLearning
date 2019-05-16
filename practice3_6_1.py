import sys
from dataset import mnist as mn

(x_train, t_train), (x_test, t_test) = \
    mn.load_mnist(flatten=True, normalize=False)

print(x_train.shape)  # (60000, 784)
print(t_train.shape)  # (60000,)
print(x_test.shape)
print(t_test.shape)
