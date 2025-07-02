# syntax  result = [expression for item in iterable if condition]

list=[2,4,1,7,12]
result = [x**2 for x in list]
print(result)

# condition in list comprehension
result2 = [y for y in list if y%2==0]
print(result2)

#creating a list by comprehension
list2= [x-2 for x in range(5)] #start with 0 
print(list2)    

name = "--Falgun Sharma--"
new_name = name.strip("--")
print(new_name) #remove leading and trailing spaces


lidt3=[[1,2,3],[4,5,6],[7,8,9]]
# flattening a list of lists
flat_list = [num for s_list in lidt3 for num in s_list]
print(flat_list)


student_names = []
print(student_names) #empty list

n = int(input("Enter a number o element"))
for i in range(n):
    
    name= input(f"take a name {i+1}")
    student_names.append(name)
        
print(student_names)

list=  ["apple", "banana", "cherry","hello ghost"]
list2=[2,4,1,7,12]
print(list)
list [2] = "Hello my list"
print(list)

print(list[1])

print(len(list))
print(list[2])
print(list[-3])

if "hello ghost" in list:
    print(f"element exist")
else:
    print("no element")

list.append("ghost")
print(list)
print(list.count("apple"))

list.extend(list2)
print(list)

print(list.index(4))
print(list)

list.insert(6,24)
print(list)

square = [x**2 for x in range (1,6)]
print(square)

#nested list 
list3 = [[1,2,3],[4,5,6,],[7,8,9]]
print(list[2][2])

list3[0][0] = "falgun"
list3[0][1] = 26
list3[0][2] = 1999
print(list3)



