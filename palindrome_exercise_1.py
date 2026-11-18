number= int(input("enter any five digit number"))
index= 0
original= number

while number > 0 :
    digit= number % 10
    index= index * 10 + digit
  
    number= number // 10

print(index)

if original == index:
    print("a palindrome number")
else:
    print("not a palindrome number")


