# Arithmetic progression 
# Same common difference 
# nth term of A.P = a + (n-1)d
# How it is arrived 
# (a) (a + d) (a + 2d) (a +3d)  .... a+(n-1)d
a = int(input("Enter first term"))
d = int(input("Enter common difference"))
n = int(input("Enter no of terms "))

res = a + (n-1)*d
print(res)