text="this is a test to remove duplicate words this test is simple"

split=text.split

print(set(split))


text1="this simple text remove duplicate words"

texts=set(text.split(" "))
text1=set(text1.split(" "))


print(texts.issubset(text))





