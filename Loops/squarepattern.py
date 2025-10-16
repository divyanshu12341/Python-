# Print a square pattern from 1* ** *** ****
n = int(input("Enter a number"))
for el in range(1,n+1):
    for el in range(1,n+1):
        print("*",end = " ")
    print()