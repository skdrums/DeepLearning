# Numpyを用いた重回帰分析
import numpy as np

# Xの定義
X = np.array([
    [2, 3],
    [2, 5],
    [3, 4],
    [5, 9],
])

print(X)

# データ数（X.shape[0]) と同じ数だけ 1 が並んだ配列
ones = np.ones((X.shape[0], 1))

# concatenate を使い、1 次元目に 1 を付け加える
X = np.concatenate((ones, X), axis=1)

# 先頭に 1 が付け加わったデザイン行列
print(X)