from re import fullmatch
    
f=open("C:\\Users\\ASUS\\Desktop\\pythonworks\\REGULAR EXPRESSION FILE WORKS\\text file")

for line in f:

    phone=line.rstrip("\n")

    pattern="(91)?[0-9]{10}"

    matcher=fullmatch(pattern,phone)

    if matcher !=None:

        print(phone)
