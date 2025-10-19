def fun():
    print("fun called")

print("Before calling fun()")
fun()
fun()
print("After calling fun()")

def printdate(d,m,y):
    print(d,m,y,sep="-")
printdate(3,4,2000)


def getdate(d,m,y):
    return d+"="+m+"="+y

print(getdate("3","4","2000"))

def fun2():
    print("Inside fun2()")
def fun1():
    print("Inside fun1()")
    fun2()
    print("After fun2()")

print("Before fun1()")
fun1()
print("After fun1()")

def sum():
    # here x and y are local variables and when we create it again,new copy is created
    x=5
    y=10
    x = x+5
    print(x,y)

sum()
sum()