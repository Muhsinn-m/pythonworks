# read the number and check it petfect number


num=int(input("enter number"))

total=0

for i in range(1,num):

    if num%i==0:

        total+=i

print("perfect number" if total==num else "not perfect number")


  