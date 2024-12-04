from re import finditer

text= "i have 3 cars,2bikes and 1 bicycle"

patern="[^a-zA-Z0-9]"

matcher= finditer(patern,text)


for obj in matcher:

    print(obj.start(),"==>",obj.group())



