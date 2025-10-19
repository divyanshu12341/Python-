n = int(input("Enter a number"))

def isPrime(x):
    for i in range(2,x-1):
        if x%i == 0: return False
    return True 

for x in range(2,101):
    if n%x==0 and isPrime(x):
        print(x)
        n = n//2


