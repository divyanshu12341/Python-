# Here we need to use nested loops to print table from 1 to 10
i = 1
for el in range(1,11):
    print(el,end = ":")
    for el in range(1,11):
        print(el*i,end = ",")
    print(" ")
    i = i+1

#Another way 
x = 10
y = 10
j=1
for el in range(1,11):
    for el in range(j,10*j+1,j):
        print(el,end = " ")
    print()
    j =j+1
