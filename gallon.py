gallons_used = 0
miles_driven = 0

while gallons_used != -1:
    gallons_used = int(input("Enter gallon used: "))

    miles_driven = int(input("Enter miles driven: "))

    result = miles_driven // gallons_used

    print(result)
    
