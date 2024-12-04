#create dictionary emloye with keys id, name,salary,department,experiance

employe={"key id":369,"name":"arjun","salary":45000,"department":"accounts","experiance":10}

print(employe)

#add contact no 251126

employe["contact"]=251126

print(employe)

#if experiance>5 update employe salary as current salary +1000.else  current salary+5000

if employe["experiance"]>5:

    employe["salary"]+=10000

else:
    employe['salary']+=5000
 
print(employe)

#add role as SDE if exp>5 else add role as JDE

if employe["experiance"]>5:
    employe["role"]="SDE"

else:
    employe["role"]="JDE"

print(employe)