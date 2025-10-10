#Print function in python 
#Function is set of instruction which take some parameters/input and do some work on parameters and 
# produces output 
# Print used to print something on screen and something on a file 
# When we do not provide any parameter to print parameter than it prints blank line
print("Hello")
print("Welcome","to","gfg")
print()
print("Hope you are enjoying python")

#end and sep in python 
#sep means separator here we can specify a separator between multiple statements 
print("Welcome",end = "")
print("to gfg")
print("25","08","2020",sep = "-")
print(10,20,30,sep = "+",end = "")

#Input function in python 
name = input("Enter your name ")
age = input("Enter your age ")
print("Welcome " + name)
print("Your age is " + age)

#Python program for addition 
x = input("Enter your first number")
y = input("Enter your second number")
#Input function always returns string 
x = int(x)
y = int(y)
sum = x + y
print(sum)

#Python program for subtraction 
x = int(input("Enter first number"))
y = int(input("Enter second number"))
diff = x - y
print(diff)

