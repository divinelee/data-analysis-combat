'''
假设一个团队里有 5 名学员，成绩如下表所示。
你可以用 NumPy 统计下这些人在语文、英语、数学中的平均成绩、最小成绩、最大成绩、方差、标准差。
然后把这些人的总成绩排序，得出名次进行成绩输出。
'''
import numpy as np
scoretype = np.dtype({'names':['name','chinese','english','math'],
						'formats':['S32','i','i','i']})
peoples = np.array([('Zhangfei',66,65,30),('Guanyu',95,85,98),('Zhaoyun',93,92,96),
					('Huangzhong',90,88,87),('Dianwei',80,90,90)],dtype=scoretype)

name = peoples[:]['name']
chinese = peoples[:]['chinese']
english = peoples[:]['english']
math = peoples[:]['math']

def show(name,a):
	print('{} | {} | {} | {} | {} | {}'.format(name,np.mean(a),np.amin(a),np.amax(a),np.var(a),np.std(a)))

print("科目 | 平均成绩 | 最小成绩 | 最大成绩 | 方差 | 标准差")
show("语文",chinese)
show("英语",english)
show("数学",math)

print("排名")
print(sorted(peoples,key=lambda x:x[1]+x[2]+x[3],reverse=True))