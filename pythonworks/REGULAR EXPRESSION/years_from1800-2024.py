from re import fullmatch

year=input("enter year :")

pattern="((18|19)[0-9]{2}|200[0-9]|201[0-9]|202[0-4])"

matcher=fullmatch(pattern,year)

if matcher==None:

    print("Invalid Year")

else:

    print("Valid Year")

    