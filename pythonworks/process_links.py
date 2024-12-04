from re import findall

f=open("C:\\Users\\ASUS\\Desktop\\pythonworks\\REGULAR EXPRESSION FILE WORKS\\text file\\sample (1).txt")

contant=f.read()
    
pattern="https?://[\w\S./]+"

urls=findall(pattern,contant)

for url in urls:

    print(url)