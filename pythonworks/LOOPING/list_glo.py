arr=[100,200,300,400,500,600,700,800]

odd_position_element=[arr[i] for i in range (len(arr)) if i%2!=0]

print(odd_position_element)

for i in range (1,len(arr),2):

    element=odd_position_element.pop()

    arr[i]=element

print(arr)




#another method

arr=[100,200,300,400,500,600,700,800]

left=1

right=len(arr)-1


if right%2==0:

    right-=1

while(left<right):

    arr[left],arr[right]=arr[right],arr[left]

    left+=2

    right-=2

print(arr)

