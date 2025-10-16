#Take a number and print smallest divisor greater than one 
n = int(input("Enter a number"))
for el in range(2,n+1):
    if(n%el == 0):
        print(el)
        break
