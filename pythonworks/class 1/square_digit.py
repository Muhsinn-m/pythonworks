num=int(input("enter number"))

total=0

while(num!=0):

    digit=num%10


    square=digit**2

    total=total+square

    num=num//10

print(total)

