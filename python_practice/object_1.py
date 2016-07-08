#!/usr/bin/env python3

class student(object):
	def __init__(self, name, birthyear):
		self.__name = name
		self.__birthyear = birthyear 

	def age(self, thisyear):
		tmp_1 = thisyear - self.__birthyear + 1
		self.age = tmp_1 
		print("%s is %s years old" %(self.__name, tmp_1) ) 

	# get name
	def get_name(self):
		return self.__name
	
	# modify birthyear 
	def mod_birth(self, date):
		# birthday
		tmp = self.__birthyear
		self.__birthyear = date
		# age 
		self.age = self.age + tmp - date 
		print("%s actually is %s years old" %(self.__name, self.age) ) 


class bachelor(student):
	description ="bachelor means an univervisity of college"

	def __init__(self, name, birthyear):
		self.__name = name
		self.__birthyear = birthyear 

	# get name ??? 
	def get_name(self):
		tmp_2 = 'Dr.'+self.__name
		return tmp_2

	# graduate 
	def get_graduate_year(self):
		return self.__birthyear + 22

# input to build object 
name = input("Student's name:")
birthyear = int(input("Student's Birthyear:"))

# judge bachelor
bachelor_judge = input("please input whether he is an undergraduate(yes/no)")

if bachelor_judge == "yes":
	s1 = bachelor(name, birthyear)
	# set GPA 
	s1.GPA = 4.1
	# method- output
	bachelor.description = "This is a changed description"
	print("%s, %s 's GPA: %s" %(bachelor.description, s1.get_name(), s1.GPA) ) 
	# output gradute year 
	print("He/She is supposed to graduate at %s" %s1.get_graduate_year() )
else: 
	# just output equally
	s1 = student(name, birthyear)
	thisyear = 2016 
	s1.age(thisyear)
	# change the birthyear 
	s1.mod_birth(1996)



