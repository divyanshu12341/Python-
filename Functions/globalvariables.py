def fun():
    a = 10
    b = 20
    print(a,b,c,d)

c = 30
d = 40
print(c,d) #a,b are not accessible hee as they are local to function fun()

def fun1():
    x = 10

x=15
fun1()
print(x)

def fun2():
    global y
    y = 10

y = 15
fun2()
print(y)

def fun3():
    x = 10
    globals()['x'] = 20
    print(x)
x =15
fun3()
print(x)
