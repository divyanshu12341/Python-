n = int(input("Enter a number"))
count = 0
while n>0:
    count = count+1
    n = int(n/10)
print(count)

count = 0
n = int(input("Enter a number"))
while n>0:
    count = count+1
    n = n // 10
print(count)