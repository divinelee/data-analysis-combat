# 统计函数 统计数组中的加权平均值 average()

import numpy as np
a = np.array([1,2,3,4])
wts = np.array([1,2,3,4])
print(np.average(a))
print(np.average(a,weights=wts))