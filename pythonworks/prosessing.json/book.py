from json import load


f=open("C:\\Users\\ASUS\\Desktop\\pythonworks\\FILE OPERATION\\book.json")

data=load(f)

all_titles=[book.get("title") for book in data]

# print(all_titles)   




pages_filter=[book.get("title") for book in data if book.get("pages") <250]

# print(pages_filter)




all_genre=[book.get("genre") for book in data ]

# print(set(all_genre))


costly_book=max(data,key=lambda d: d.get("price"))

# print(costly_book)

all_authors=[book.get("author") for book in data]

author_count={auth:all_authors.count(auth) for auth in all_authors}

print([k for k,v in author_count.items() if v > 1])





              


