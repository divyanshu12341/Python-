#id function gives ideo of an object 
#id function gives unique identifier for every object 
#id provides address of an object 
print(id(5))
#In python if value of literals are same they point to same memory location 
a = 10 
b = 10
print(id(a))
print(id(b))
c = "geek"
d = "geek"
print(id(c))
print(id(d))
#is operator in python checks if identities of two operands are same or not 
a = 10
b = 10
print(a is b) #true
c = a 
print(c is a) #true
c = 20
print(c is b) #false