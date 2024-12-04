# element count

text="ZABABBCCDDE"

character_frequency={ch:text.count(ch) for ch in text}

print(character_frequency)

#print non recursive ekemets

for k,v in character_frequency.items():

    if v==1:

     print(k)


