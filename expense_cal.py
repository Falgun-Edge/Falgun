exp = {}

while True:
    item = input("Enter the expense item or type 'done' to finish: ")
    if item.lower() == 'done':
        break
    try:
        amnount = float(input(f"Enter the amount for {item}:"))
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        continue
    
    if item in exp:
        exp[item] += amnount
    else:
        exp[item] = amnount

print("\nExpense Summary:")
for item, amount in exp.items():
    print(f"{item}: RS {amount:.2f}")

total_expense = sum(exp.values())
print(f"\nTotal Expense: RS {total_expense:.2f}")



print(exp)