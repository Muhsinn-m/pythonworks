arr=[2,4,6,3,8,7]

serch_element=int(input("enter number"))

ispresent=False

for i in range(0,len(arr)):

    if serch_element==arr[i]:


        ispresent=True

    break

print(ispresent)
