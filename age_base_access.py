try:
    age = int(input("Enter your age:"))
except ValueError:
    print("Invalid Input. please enter a number value")
else:
    if age == 18 or age > 18:
        print("You are eligible to vote .")
    else:
        print("You are underage to vote.")


if age >21:
    print("You can buy alcohol")  
elif age == 21:
    print("You can buy alcohol with less than 5%, alcohol content")
else:
    print("You cannot buy alcohol")