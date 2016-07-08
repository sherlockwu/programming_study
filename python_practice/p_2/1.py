#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

def randomgenerate():
	sequence = []
	set_1 = "0123456789" + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	# 10 bit 
	for k in range(1,11):
		temp = random.choice(set_1)
		sequence.append(temp)
	# 
	return sequence

def judge(sequence, L):
	for k in range(0, len(L)):
		result_1 = True
		for j in range(0, 10):
			if L[k][j]!= sequence[j]:
				result_1 = False
		if result_1:
			return True
	return False

def generate(f, count):
	# while compare 
	number = 0 
	L = []
	while number<count:
		# random generate 
		sequence_1 = randomgenerate() 
		# compare
		result_1 = judge(sequence_1, L) 
		if result_1==False:
			L.append(sequence_1)
			number = number + 1 	
			# write into file 
			f.write(''.join(sequence_1)+'\n' ) 


filename = "./output.txt"
f = open(filename, "w")
count = 200

# generate 
generate(f, count)
f.close()
# print 
print("These Codes have been stored in File %s" %filename)