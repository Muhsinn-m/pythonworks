from re import fullmatch,finditer

f=open("C:\\Users\\ASUS\\Desktop\\pythonworks\\REGULAR EXPRESSION FILE WORKS\\text file\\social_posts.txt")

for line in f:

    words=line.rstrip("\n")
    
    pattern="#\w+"

    matcher=finditer(pattern, words)

    for obj in matcher:
        
        print(obj.group())





        