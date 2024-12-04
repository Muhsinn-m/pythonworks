from json import load


f=open("C:\\Users\\ASUS\\Desktop\\pythonworks\\FILE OPERATION\\employe.json")

data=load(f)


for emp in data:

    print(emp)

