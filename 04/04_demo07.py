# 统计函数 统计数组中的中位数 median()、平均数 mean()

import numpy as np
a = np.array([[1,2,3],[4,5,6],[7,8,9]])

# 求中位数
print(np.median(a))
print(np.median(a,0))
print(np.median(a,1))

# 求平均数
print(np.mean(a))
print(np.mean(a,0))
print(np.mean(a,1))