arr=[100,200,300,400,500]

k=1

for i in range(1,k+1):

    poped_element=arr.pop()

    arr.insert(0,poped_element)

print(arr)