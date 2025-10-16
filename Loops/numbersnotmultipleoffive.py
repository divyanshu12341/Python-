# Numbers not multiple of 5 
# We use continue keyword to move to next iteration 
l = [10,16,17,18,19,15]
for el in l: 
    if(el % 5 ==0):
       continue
    print(el)

i = 0

#Another example of continue keyword
while(i<=5):
    if(i==3):
        i = i+1
        continue
    print(i,i*i)
    i = i+1

#Another example of continue keyword 
l = [10,16,17,18,9,15,21,13]
for x in l:
    if x%5 == 0:
        continue
    if x%7 == 0:
        break
    print(x)
print("Bye")