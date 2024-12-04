num=int(input("enter the number"))

prev=0

is_fibo=False

for i in range (1,num+1):

    next=prev+current

    prev=current

    current=next

    if next==num:

        is_fibo=True

        break


