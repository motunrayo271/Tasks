number= 65432

while number > 0:
    digit= number % 10
    print(digit , end="\t")

    number= number // 10


