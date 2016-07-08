#!/usr/bin/env python3
import math


def judge_prime(number):
	# 计算 quad
	tmp = int(math.sqrt(number))
	i = 2
	# 依次判断
	while i <= tmp:
		# 如果有一个就立马return False
		if number%i==0:
			return False
		i = i + 1 
	# 否则return True
	return True

print('''你好
	欢迎使用''');
name = input("Hi, please input your name:")
count = int(input("Then, please input a number:"))
if count>=100:
	print("please input a number < 100")
	print("End")
else:
	print("hello ",name,",then we will print the prime number < %d" %count)
	i = 2  
	count_prime = 0
	while i< count: 
		# judge prime 
		result_prime = judge_prime(i)  
		# output 
		if result_prime == True: 
			print(i)
			count_prime = count_prime + 1
		# x++ 
		i = i + 1 
	print("%d prime numbers" %count_prime)
		
print ("Bye %s from" %name ) 
