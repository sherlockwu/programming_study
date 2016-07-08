#! /usr/bin/env python3



# This object program is to try multi-inheritance



# class animal

class animal(object):
	description="This is smartest thing in the earth."
# class runnableMixIn 
class runnableMixIn(object):
	def get_to(self, destination):
		print("ran to %s" %destination)

# class flyableMixIn 
class flyableMixIn(object):
	def get_to(self, destination):
		print("flied to %s" %destination)

# sub-class panda 
class panda(animal, runnableMixIn):
	def __init__(self, age, gender):
		self.age = age
		self.gender = gender


# sub-class penguin 
class penguin(animal, flyableMixIn):
	pass 





Kan = panda(22, "male")
Kan.get_to("Nanjing")

Sherlock = penguin()
Sherlock.get_to("HongKong")
