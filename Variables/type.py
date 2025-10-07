#type is a built in function that tells about data type of variable  
a = True
print(type(a))
#None means no value is assigned to a variable
b = None
print(type(b))
# Sequences
str = "gfg"
print(type(str))
# List 
l = [10,20,30]
print(type(l))
#Tuple 
# THESE ARE IMMUTABLE 
c = (10,20,30)
print(type(c))
#Set 
#Collection of items where all items are distinct 
# Order does not matter it has own internal way of storing items 
# Set mainly internally uses hashing 
s = {10,20,30}  #set
print(type(s))
# Dictionary 
# Collection of key value pairs and internally use hashing 
dict = {10:"gfg",20:"pw"}
print(type(dict))