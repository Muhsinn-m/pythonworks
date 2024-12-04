from re import finditer

text= "i have 3 cars,2bikes and 1 bicycle"

patern="[a-z]"

matcher= finditer(patern,text)


for obj in matcher:

    print(obj.start(),"==>",obj.group())



