arr=[20,21,22,23,24,25]

is_present=False

search_element=int(input("ENTER A NUMBER  "))

low=0

up=len(arr)-1


while (low<=up):
    
    mid=(low+up)//2

    if search_element==arr[mid]:
        is_present=True
        break

    elif search_element<arr[mid]:
        up=mid-1

    elif search_element>arr[mid]:
        low=mid+1

print(is_present)







