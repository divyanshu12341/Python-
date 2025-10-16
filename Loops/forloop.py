#for x in seq
# Statement-1
# Statement-2
#items through which we can iterate is called iterables in python 
#seq can be list,tuples,dictionary 
#there is no basic for-loop where there is initialization then condition then incrementdecrement 
l = [10,20,30,40]
for x in l:
    print(x)

s = "gfg"
for x in s:
    print(x)

print("Multiple print statements with for loop now: ")

for x in s:
    print(x)
    print(x)

#Printing numbers from 0 to 20 multiple of 6 
print("Now printing multiple of 6: ")
for x in range(20):
    if x%6==0:
        print(x)

print("Now printing list items")
l = [10,20,30,40]
for i in range(len(l)):
    print(l[i])

print("Now printing elements along with index")
l = [10,20,30,40,50,60]
for i in range(len(l)):
    print(i,l[i])