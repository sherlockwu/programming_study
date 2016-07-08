#!/usr/bin/env python3

def Hannoi(n, t_from, t_buffer, t_to):
	# 递归边界
	if n==1:
		print("move from %s to %s" %(t_from,t_to))
		return 
	# 递归求解
	Hannoi(n-1, t_from, t_to, t_buffer)
	Hannoi(1, t_from, t_buffer, t_to)
	Hannoi(n-1, t_buffer, t_from, t_to)





# input sth 
print("this is a program on 3 Hannoi_Tower problem")
n = int(input("Please set the number of plates in A tower"))

# call function cal 
Hannoi(n, 'a', 'b', 'c')



# output 
print("That's all, thanks!")