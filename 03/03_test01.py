'''
题目：A+B
输入格式：有一系列的整数对 A 和 B，以空格分开。
输出格式：对于每个整数对 A 和 B，需要给出 A 和 B 的和。
'''

while True:
	try:
		line = input()
		a = line.split()
		print (int(a[0]) + int (a[1]))
	except:
		break