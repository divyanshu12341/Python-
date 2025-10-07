x =100 
y = 200 
print("Before swapping: ",x,y)
# Swapping code 
z = x 
x = y 
y = z
print("After swapping: ",x,y)

# In python
x = 100 
y = 200 
x,y = y,x
print("After swapping ",x,y)

x = 100
y = "geeks"
x,y = x+5,y+"for"
print("After modification, ",x,y)