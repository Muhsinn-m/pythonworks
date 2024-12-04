num1=int(input("enter num 1"))
num2=int(input("enter num 2"))
num3=int(input("enter num 3"))

if num1>num2 and num1>num3:
    if num2>num3:

     print("num2 is second largest number")
     
    else:
     
     print("num 1 is second largest number")



if num2>num1 and num2>num3:   
    if num1>num3:

     print("num1 is secomd largest number")

    else:
     print("num3 is second largest number")

    
if num1==num2==num3:
  
    print("those numbers are equal")
