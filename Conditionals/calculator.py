import sys
print(""" Please select operation: 
1) Add
2) Subtract
3) Multiply  """)
choice = int(input("Select operation from 1,2 or 3"))
if choice not in (1,2,3) : 
    print(end=" ")
    print("Invalid choice",end=" ")
    sys.exit()
a = int(input("Enter first number"))
b = int(input("Enter second number"))
if(choice == 1):
    res = a+b
elif(choice == 2):
    res = a-b
elif(choice == 3):
    res = a*b
print("Result is ",res)