year=int(input("enter a year"))

# rem=year%4

if (year%100!=0 and year%4==0) or (year%100==0 and year%400==0):
    
    
    print("the entered yer is leap year")

else:
    print("the enetered number is not leap year")
    

 

