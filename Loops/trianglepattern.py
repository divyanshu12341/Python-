n = int(input("Enter a number"))
for el1 in range(1,n+1):
    for el2 in range(1,n+1):
        if el2<=el1:
            print("*",end=" ")
    print()

print("Alternative method: ")

for element1 in range(1,n+1):
    for element2 in range(1,element1+1):
        print("*",end=" ")
    print()