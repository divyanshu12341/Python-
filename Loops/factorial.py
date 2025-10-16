n = int(input("Enter a number"))
if n ==0:
    print(1)
else:
    product = 1
for el in range(1,n+1):
    product = product*el

print(product)

#using library function
import math
n = int(input("Enter n"))
res = math.factorial(n)
print("Factorial is ",res)