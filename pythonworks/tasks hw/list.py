list1=["apple", "orange", "mango", "onion",]

list2=[100,200]

result={}

for i in range(0,len(list2)):

    list_one_index_element=list1[i]
    
    list_two_index_element=list2[i]

    result[list_one_index_element]=list_two_index_element

balance_element=list1[len(list2):]

for index,element in enumerate(balance_element):
    
    result[element]=index+1

print(result)
                









