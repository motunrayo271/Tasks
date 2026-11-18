
digit_1 = float(input("Enter first number"))
digit_2 = float(input("Enter Second number"))
digit_3 = float(input("Enter third number"))

if digit_1 > digit_2:
    temp = digit_1
    digit_1 = digit_2
    digit_2 = temp

if digit_2 > digit_3:
    temp = digit_2
    digit_2 = digit_3
    digit_3 = temp

if digit_1 > digit_2:
    temp = digit_1
    digit_1 = digit_2
    digit_2 = temp

print("number in ascending order")
