from re import fullmatch

date=input("enter a date=>")

pattern="(0?[1-9]|[12][0-9]|3[0-1])"

matcher=fullmatch(pattern,date)

if matcher==None:
    print("Invalid date")

else:
    print("Valid date")
