'''str = "hello world"
for i  in range(5):
    print(str)

for i in range(1, 10):
    print(i)

num = int(input("Enter a number whose multiplication table you want: "))
length = int(input("ENTER A LENGHT OF MULTIPLICATION TABLE: "))

for x in range (1, length+1):
    print(f"{num} x {x} = {num*x}")

count = 0
x= int(input("Enter a number:"))
for i in range(1, x+1):
    count += 1
    print(count)
    
x= int(input("Enter a number:"))
for i in range(1, x+1):
    count -= 1
    print(count)

x = int(input("Enter a number to check even series: "))
for i in range(1, x+1):
    if i%2==0:
        print(f"{i} is even")
        print(f"{i}k")

x = int(input("Enter a number to check odd series : "))
for i in range(1, x+1):
    if i%2!=0:
        print(f"{i} is odd")



for i in range (1, 101):
    if i % 5 == 0:
        print(i)

num1 = int(input("Enter a number: "))
for i in range (0,num1+num1):
    num1 = num1-0.5
    print(num1)'''

x = int(input("Enter a number to checkseries : "))
for i in range(1, x+1):
    if i%2==0:
        print(f"{i} is even")
    elif 1%2!=0: 
        print(f"{i} is odd")