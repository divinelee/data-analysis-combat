# 统计函数 计数组 / 矩阵中的最大值函数 amax()，最小值函数 amin()

import numpy as np
a = np.array([[1,2,3],[4,5,6],[6,7,8]])
print(np.amin(a))
print(np.amin(a,0))
print(np.amin(a,1))
print(np.amax(a))
print(np.amax(a,0))
print(np.amax(a,1))