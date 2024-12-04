#dictionory methods
#emloye id, name,department,age,salary

employe={"id":369,"name":"muhsin","department":"hr","salary":25000}


#method 1  GET()

print(employe.get("department"))   #invalid key returns none


#method 2  POP()

employe.pop("salary")

print(employe)     #pop is a function to remove a key from the dictionary

#method 3  KEYS()

for k in employe.keys():

    print(k)       #print only keys no values


#method 4  VALUES()

for v in employe.values():

    print(v)       #print only values no keys


#method 5  ITEMS()

for k,v in employe.items():

    print(k,v)        #print keys and values together
    
