#find the max two num

max_two=lambda str1,str2:str1 if len(str1)>len(str2) else str2

print(max_two("hai","helloo"))

#find the min two

min_two=lambda str3,str4:str3 if len(str3)<len(str4) else str4

print(min_two("bike","car"))