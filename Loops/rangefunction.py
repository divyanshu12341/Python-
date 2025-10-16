#It generates range from 0 to 5-1
#range function gives object not list we can construct a list using this object
r = range(5)
print(r)
l = list(r)
print(l)

#type of object returned by range is <class,range>
print(type(r))

#Generate a numbers from 10 to 19
r = range(10,20)
print(r)
l = list(r)
print(l)

r = range(-2,2)
l = list(r)
print(l)

#Range function with three parameters --> range(x,y,z)
# [x,x+z,x+2z, ... ]
r = range(10,20,3)
l = list(r)
print(l)

r = range(20,10,-2)
l = list(r)
print(l)

r = range(20,10,-3)
l = list(r)
print(l)