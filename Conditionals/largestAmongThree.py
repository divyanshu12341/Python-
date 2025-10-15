a = int(input("Enter a"))
b = int(input("Enter b"))
c = int(input("Enter c"))
if(a ==b == c):
    print("All is equal")
elif(a>=b and a>=c):
    print("a is largest")
elif(b>=a and b>c):
    print("b is largest") 
elif(c>=a and c>=b):
    print("c is largest") 
