num1=int(input("enter first number"))

num2=int(input("enter second number"))

max_num=max(num1,num2)

for i in range(max_num,(num1*num2),max_num):

    if i%num2==0 and i%num1==0:


        print(i)
        break
