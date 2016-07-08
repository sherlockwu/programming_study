#! /usr/bin/env python3
from types import MethodType

# 一个叫 py 的类
class py(object):
	
	# private version 
	
	# get_version 
	@property 
	def version(self):
		return self.__version
	# set_version 

	@version.setter
	def version(self, ver_in):
		# judge
		## int
		if not isinstance(ver_in, float):
			raise ValueError("Not an number")
		
		## <10?
		if (ver_in>0) and (ver_in<10):
			# set
			self.__version = ver_in
		else:
			#  raise
			raise ValueError("Must 0<k<10") 

	

	
	# print 
	def py_print(self, str_1):
		print(str_1)





def f_author(self):
	print("Author: Kan")


# 实例
int_1 = py()


## try on __slots__
int_1.description = "This is a emulated python intepreter."
print(int_1.description)


int_1.print_author = MethodType(f_author, int_1)
int_1.print_author()

## try operater
### normal method 
#int_1.set_version(1.0)
#print("Intepreter Version: %s" %(int_1.get_version()) )  
### operator 
int_1.version = 1.2
print("Intepreter Version: %s" %(int_1.version) )  





# print 
int_1.py_print("Hello World!")


# 用他尝试一些 