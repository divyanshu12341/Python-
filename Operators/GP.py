# 
# Series with common ratio between consecutive terms 
# nth term of GP = ar to power of n-1
a = int(input("Enter first term"))
r = int(input("Enter common ratio"))
n = int(input("Enter  all terms "))
res = a*r**n-1
print(res)