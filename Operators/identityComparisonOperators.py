#is/is not 
# it checks for ids for both operands means both should be stored in same memory location 
x = 10
y = x 
print(x is y)
print(x is not y)

#if value is same it points to same memory location 
x1 = 10
x2 = 10

y1 = "geeks"
y2 = "geeks"

z1 = 10.5
z2 = 10.5

print(x1 is x2)
print(y1 is y2)
print(z1 is z2)

l1 = [10,20,30]
l2 = [10,20,30]
print(l1 is l2) #false as only for literals it points to same memory location for same values not for collections 
