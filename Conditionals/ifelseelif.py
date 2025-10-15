#Program for even odd 
n = int(input("Enter a number"))
if(n%2==0):
    print("Number is even")
else :
    print("Number is odd")


#Program for positive,negative or zero
if(n==0):
    print("Number is zero")
elif(n>0):
    print("Number is positive")
elif(n<0):
    print("Number is negative")

#Program for positive even,positive odd,negative even,negative odd,zero
if(n==0):
    print("Zero")
if(n>0):
    if(n%2==0):
        print("Positive even")
    else:
        print("Positive odd")
if(n<0):
    if(n%2==0):
        print("Negative even")
    else :
        print("Negative odd")