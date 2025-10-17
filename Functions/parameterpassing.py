def fun(x):
    print(id(x))
    x = 15
    print(id(x))
x = 10
fun(x)
print(id(x))
print(x)

def func1(l):
    print(id(l))
    l.append(15)
    print(id(l))
l = [5,10,25]
func1(l)
print(id(l))
print(l)

def func2(l):
    l = [40,50]

l = [10,20,30]
fun(l)
print(l)