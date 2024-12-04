start=int(input("enter starting number"))

end=int(input("enter ending number"))

if start<end:

    for num in range(start,end+1,1):

        print(num)

else:
    for num in range(start,end-1,-1):

        print(num)
