import numpy as np

a = np.array([1, 2, 3])
print(a.shape)  # 形
print(a.ndim)  # 次元数

b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(b)
print(b.shape)
print(b.ndim)
print(b.size)  # サイズ

a = np.zeros((3, 3))
print(a)

a = np.ones((2,3))
print(a)

a = np.full((2,3),8)
print(a)

a = np.eye(5)
print(a)

e = np.random.random((4,5))
print(e)

val= e[0,1] # eの行列から1行２列目の値を得る
print(val)
center = e[1:3,1:4] # １行目〜３行目まで（３行目は含まない）＆１列目から４列目まで（４列目は含まない）の選択
print(center)
e[1:3,1:4]=0 # 指定部に０を代入
print(e)

a = np.arange(3,10,1) 
print(a)

a=np.random.randint(0,10,(2,1,3)) # 0 ~ 9 の範囲の値をランダムに用いて埋められた (2, 1, 3) と (3, 1) という大きさの配列を作る
print(a)