from re import fullmatch

email=input("enter email:")

pattern="[a-z]+[a-z0-9]{5,63}@gmail.com"

matcher=fullmatch(pattern,email)
                
print("invalid email" if matcher==None else"valid email")

