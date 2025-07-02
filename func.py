'''#1
def name(): # creating the function
    print("Falgun Sharma")

name() # calling the function

#2
def fl_name(f_name,l_name):
    print(f"{f_name} {l_name}")

fl_name("Basket","MAZE") # calling the function with parameters

#3 arbitary Arguements

def friends(*args):# *agrs =tuple
    print("My eldest friend is", args[1])

friends("falgun","vaibhav","prakhar")

def friends2(**args):#Arbitrary Keyword Arguments, **kwargs= dictionary
    print("My eldest friend is", args["eldest"])

friends2(eldest="Falgun", middle="Vaibhav", youngest="Prakhar")

def default_args(name="Falgun", age=20):
    print(f"Name: {name}, Age: {age}")

default_args()  # calling with default values
default_args("Vaibhav", 22)  # calling with custom values   
'''

def fun (n):
    return lambda a : a*n

multi = fun(2)

print(multi(10))