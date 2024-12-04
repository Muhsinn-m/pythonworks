from re import finditer

text="7894561230"

matcher=finditer("[0-1]",text)

for obj in matcher:

    print(obj.start(), obj.group())
    