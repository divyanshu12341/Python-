
def findfirstdigit(x):
    rem = 0
    while(x>=10):
        x = x//10
    print(x)

x = int(input("Enter a number"))
findfirstdigit(x)
