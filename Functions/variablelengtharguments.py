
# * symbol used for multiple length arguments 
def sum(* elements):
    res = 0 
    for x in elements:
        res = res+x
    return res

print(sum(10,20))
print(sum(10,20,25,35,45,11,22,33,1456))

def sum_initial(initial_sum,* elements):
    res = initial_sum
    for x in elements:
        res = res+x
    return res

print(sum_initial(5,10,20))

def printElements(* element):
    print(element)

printElements(101,"abc",100)
printElements(102,"def",104)

#keyword variable length arguments 
# **symbol recieved as a dictionary in function 

def printDetails(** details):
    for d,v in details.items():
        print(f"{d} is {v}")

printDetails(id=101,name="abc",price=100)

def printDetailsWithid(id,** details):
    print(f"Details of id:{id}")
    for d,v in details.items():
        print(f"{d} is {v}")

printDetailsWithid(101,name = "Headphones",price = 200)
print()
printDetailsWithid(102,name = "Earphones",price = 300)

