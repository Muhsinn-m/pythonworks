from re import finditer

text= "i have 3 cars,2bikes and 1 bicycle"

patern="[^ak, 0-9A-Z]"

matcher= finditer(patern,text)


for obj in matcher:

    print(obj.start(),"==>",obj.group())