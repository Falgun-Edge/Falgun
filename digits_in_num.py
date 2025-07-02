def digits_count():
    num = int (input("Enter a number" ))
    count = 0
    while num >0:
        digit = num %10
        count = count +1
        num = num //10
    return count

print(digits_count())