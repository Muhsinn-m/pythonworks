from re import finditer

text="fatcatrunservyfasttocaththerat"

matcher=finditer("at",text)

for obj in matcher:

    print(obj.start(), obj.group())
    