# 统计函数 统计数组的百分位数 percentile()

import numpy as np
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.percentile(a,50))
print(np.percentile(a,50,axis=0))
print(np.percentile(a,50,axis=1))