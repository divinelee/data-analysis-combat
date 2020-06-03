# 求 1+3+5+7+…+99 的求和，用 Python 该如何写？

sum = 0
for number in range(1,100,2):
	print (number)
	sum = sum + number
print (sum)