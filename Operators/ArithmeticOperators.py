# Arithmetic operators in python 
x = 9
y = 4
print(x+y)  #13
print(x-y)  #5
print(x*y)  #36
print(x/y)  #2.5
print(x//y) #2
print(x%y)  #1
print(x **y) # 6561 x raise to power of y

x = -5
y = 2
print(x // y) #-3 as floor of -2.5 is =3

x = 2
y = -2
print(x**y) #2 to power of -2 is 1/4

# Operators precedence 
#In ascending  order 
# + -  -- lowest precedence 
# * / //
# **  -- highest precedence 
print(5 + 2*3)
print(5 + 3*4**2)

# If same precedence then associativity 
# + - --> left to right 
# * / // --> left to right 
# **  --> right to left 

print(5+4-1)
print(2**2**-1)
print((2**2)**-1)