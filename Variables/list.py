#list creates array of elements and can be accessed using indexes 
l = [10,20,30,40,50]
print(l)
print(l[0])
print(l[1])
# -1 means last item 
print(l[-1])
#Append function appends item at last of the list 
l.append(60)
print(l)
#Insert function inserts item at given index 
l.insert(1,90)
print(l)
#in operator tells whether element is present in collection or not 
print(15 in l)
print(10 in l)
# Count operator tells us how many occurences are present in list 
print(l.count(10))
#Index function tells first occurence of an item taking element as an argument 
#If item is not present then we will get an error 
# We should only call it when given item is present 
print(l.index(20))
# collection.index(element,startingIndex,endingIndex)
print(l.index,1,5);
# Remove function removes given value from a list 
# If an item is not present and we use remove function,then it will raise an error 
l.remove(10)
print(l)
# Pop will remove last item from a list
# It will return deleted value  
print(l.pop())
# We can also provide pop function in a given index
# Del keyword used to remove items 
del l[1]
print(l)
# Range of indexes 
del l[0:2]
print(l)