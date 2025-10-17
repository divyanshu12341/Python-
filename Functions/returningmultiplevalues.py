def add_multiply(x,y):
    sum = x+y
    mul = x*y
    sub = x-y
    return sum,mul,sub

s,m,sb = add_multiply(20,40)
print("Sum is ",s)
print("Multiplication is ",m)
print("Subtraction is ",sb)

def add_multiply_list(x,y):
    sum = x+y
    mul = x*y
    sub = x-y
    return [sum,mul,sub]

s,m,sb = add_multiply_list(10,40)
print("Sum is ",s)
print("Product is ",m)
print("Subtraction is ",sb)