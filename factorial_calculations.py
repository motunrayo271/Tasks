non_negative_integer = int(input("Enter a non negative integer"))

total = 1
for counter in range(1, non_negative_integer+1):
    total *= counter
    print(f"{non_negative_integer}! = {total}")

    
