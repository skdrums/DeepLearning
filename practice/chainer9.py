from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split

# 1
dataset = load_boston()

x = dataset.data
t = dataset.target

print(x.shape)

print(t.shape)

# 2
x_train, x_test, t_train, t_test = train_test_split(x, t, test_size=0.3, random_state=0)
