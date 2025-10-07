#Set contains only distinct elements 
#It is unordered 
#No Indexing 
# Union,Intersection,Set Difference are fast 
# Uses hashing internally 
s1 = {10,20,30}
print(s1)
s2 = set([20,30,40,20,40])
print(s2) #set 
s3 = {} #It does not create empty set instead dictionary
print(type(s3)) #dict
s4 = set()
print(type(s4)) #set
print(s4) #it will print set()

#Insertions in a set 
s = {10,20}
s.add(30)
print(s)
s.update([40,50])
print(s)
s.update([60,70],(80,90))
print(s)

#Removal in a set 
s = {10,30,20,40}
#if any item provided which is not present then it will do nothing 
s.discard(30) 
print(s) #10 20 40 
# if any item provided which is not present then it will raise an error 
s.discard(20) # 10 40 
print(s)
#It will remove everything from set and you get an empty set
s.clear()
print(s)
#del removes object itself 
del(s)

#Other operations in set 
s = {10,30,20,40}
print(len(s))
print(20 in s)
print(50 in s)

s1 = {2,4,6,8}
s2 = {3,6,9}
#union 
print(s1|s2)
#intersection 
print(s1&s2)
#set difference 
print(s1-s2) #Present in s1 but not in s2
#symmetric difference -- All elements except common 
print(s1^s2)