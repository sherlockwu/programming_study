#!/usr/bin/env python3

from collections import Iterable

Author = "Kan Wu"
print("This is a Python program from %s " %Author)

L = ["sher", "holme", "Hello", "1", "2"]
S = L[0::2]
S_1 = "Sherlock"[::2]


print(S_1)

print("After slice: %r" %S)


k = 0
for name in L: 
	print("%d: %r" %(k, name))
	k = k+1

for ch in "Sherlock"[::2]:
	print(ch)

d_1 = {'Sherlock':1, "Holmes":2, "Watson":3}
for number in d_1.values():
	print(number) 

test_1 = isinstance([1,2,3],Iterable) 
print(test_1)

for count, name in enumerate(L):
	print(count, name)

print("new")

#L_2=list(range(11,1,-2))
#print(L_2)

L_1 = [l*j for l in range(1,3) for j in range(3,1,-1)]
print(L_1)
for k in L_1:
	print(k)

print("new")
L_2 = [name+":"+ str(count) for name, count in d_1.items()]
print(L_2)

