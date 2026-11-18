num1= int(input("enter fist num"))
num2= int(input("enter second num"))
num3= int(input("enter third num"))



for numbers in range(4):
    total= num1+num2+num3
    float_average = float(total)/3
    product= num1*num2*num3

if num1 > num2 and num1 > num3: 
    print("largest = ", num1)
elif num2 > num1 and num2 > num3:
    print("largest = ", num2)
elif num3 > num1 and num3 > num2:
    print("largest = ", num3)


if num1 < num2 and num1 < num3:
    print("smallest = ", num1) 
elif num2 < num1 and num2 < num3:
    print("smallest = ", num2)
elif num3 < num1 and num3 < num2:
    print("smallest = ", num3)

print("total is:" ,total)
print("float_average:" f"{float_average:.2f}" )
print("product is:" ,product)









































