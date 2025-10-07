#Dictionary is basically collection of key-value pairs 
#It is unordered and all keys must be distinct 
#Values may be repeated 
#Uses hashing internally 
#It is similar to unordered map in c++ 
d = {110:"xyz",101:"abc",102:"def",103:"abc"}
print(d)
d = {}
#If key does not exist it will raise an error 
d["laptop"] = 40000
d["earphones"] = 20000
print(d)
print(d["laptop"])
#When we provide key to get function,it gives its corresponding value
d = {110:"xyz",101:"abc",102:"def",103:"abc"}
#If key not present it will give none value 
print(d.get(110))
print(d.get("laptop"))
if 125 in d:
          print(d[125])
else : 
          print("NA")
if 110 in d:
          print(d[110])
else : 
          print("NA")
d[101] = "wxy"
print(len(d))
print(d)
# print(d.pop(105))
print(d)
# del d[106]
print(d)
d[108] = "cde"
#popitem removes last inserted key-value pair 
print(d.popitem())

#type conversion in python 
#Implicit type conversion 
#Explicit type conversion 

#Example is data is in tuple which is immutable and we want to convert it into list 
#Implicit type conversion 
a = 10 #int
b = 1.5 #float
c = a+b 
print(c) #it results in float -->float + int
d = True 
e = d+a
print(e) #it result is 11 which is d+e

#Explicit type conversion
#Example 1
s = "135"
i = 10 + int(s)
print(i)
f = float(s)
print(i)
print(f)

#Example 2 
s = "geeks"
print(list(s))
print(tuple(s))
print(set(s))

#Example 3 
l = ['a','b','c']
print(str(l))
a = 10
b = 11 
print(str(a)+str(b))
c = 12.5
print(str(c))

#Example 4
t = (10,20,30)
print(list(t))
s = {10,20,30}
print(list(s))

#Prefix ; 0b is binary number 
#Prefix: 0x  is hexadecimal number 
#Prefix: 0o is octal number 
a = 20 
print(bin(a))
print(hex(a))
print(oct(a))

#Example 
a = "1001"
print(int(a,2))
b = "12"
print(int(b,8))
c = "A1"
print(int(c,16))