arr1=[2,3,5,6,7]

arr1.sort()

for i in range(0,len(arr1)-1):

    j=i+1

    result=arr1[j]-arr1[i]

    if result !=1:

        print(arr1[i]+1,"IS MISSING")

        break



