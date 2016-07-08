#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import string

def _greet_1(name):
	print("hello, %s" %name)
def _greet_2(name): 
	print("hi, %s" %name)

def greeting(name_1):
	temp_len = len(name_1)
	if temp_len<=5: 
		_greet_1(name_1)
	else: 
		_greet_2(name_1) 

def test():
	temp = sys.argv
	temp_l = len(temp)

	if temp_l == 1:  
		print("hello world") 
	elif temp_l == 2 : 
		print("hello %s" %temp[1])
	else : 
		print("too much input")  

if __name__ == '__main__' :
	test()  
