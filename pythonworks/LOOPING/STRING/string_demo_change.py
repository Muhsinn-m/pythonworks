text="hello world"

print(text.index('o'))

text="vipin@gmail.com"

print(text[0:text.index("@")])




text="hellopython"

o_index=text.index("o")

reversed_sub_str=text[o_index-1::-1]

balance_sub=text[o_index:1]

result=reversed_sub_str+balance_sub

print(result)
