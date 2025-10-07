#tuples are immutable 
#Values in tuple cannot be changed 
t = (10,20,"gfg")
print(t)
t = () 
print(type(t)) #tuple 
print(t)
t = (10) #int
print(type(t))
t = (10,) #tuple 
print(type(t))

#tuples can be created without parenthesis 
#tuple with single value 
t = 10,
#tuple with multiple values 
t = 10,20,30,40,50,10,20
print(t[2]) #30
print(t[-1]) #20 
print(t[1:3]) #20,30,40
print(len(t)) #7
print(t.count(10)) #2
print(t.index(20))#1