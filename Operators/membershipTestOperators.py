# membership test operator 
#in operator for string:it checks whether given string is substring or not 
#in operator for dictionary:it checks for key
#in operator for list,set,tuple:check for membership 

s = "geeksforgeeks"
print("g" in s)
print("for" in s)
print("gk" in s)

d = {10:"abc" , 20:"gef"}
print(10 in d)
print(15 in d)
print("gef" in d)

l = [10,20,30,15]
print(30 in l)
print([20,30] in l)
print(30 not in l)
print(40 not in l)
print([20,30] not in l)