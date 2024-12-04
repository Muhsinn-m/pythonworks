from re import fullmatch

pan_card_number=input("enter pan card number:")

pattern="[A-Z]{3}[PCAFHT][A-Z]{1}[0-9]{4}[A-Z]{1}"

matcher=fullmatch(pattern,pan_card_number)
                  
if matcher==None:

    print("Invalid PAN card number")

else:
    
    print("Valid PAN card number")
    