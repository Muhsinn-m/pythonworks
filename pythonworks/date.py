from re import findall

f=open("C:\\Users\\ASUS\\Desktop\\pythonworks\\REGULAR EXPRESSION FILE WORKS\\text file\\social_posts - Copy.txt")

date=f.read()

pattern="[0-9]{2}/[0-9]{2}/[0-9]{4}"

dates=findall(pattern,date)

for d in dates:

    print(d)
