#a. largest number

num1=int(input("enter a first number"))

num2=int(input("enter a second number"))

num3=int(input("enter a third number"))

largest=max(num1,num2,num3)
    
print("largest number is",largest)


#b. second largest

if (num1 > num2 and num1 < num3) or (num1 < num2 and num1 > num3):
    second_largest = num1
elif (num2 > num1 and num2 < num3) or (num2 < num1 and num2 > num3):
    second_largest = num2
else:
    second_largest = num3

print("The second largest number is:",second_largest)

     
#c. sort three numbers

if num1 > num2:
    num1, num2 = num2, num1
if num1 > num3:
    num1, num3 = num3, num1
if num2 > num3:
    num2, num3 = num3, num2


print("The numbers in sorted order are:", num1,num2,num3)

