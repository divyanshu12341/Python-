n = int(input("Enter a number"))
# n = 5 --> 4 spaces in left and 4 spaces in right and one in between 
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for k in range(2*i+1):
        print("*",end = " ")
    print()