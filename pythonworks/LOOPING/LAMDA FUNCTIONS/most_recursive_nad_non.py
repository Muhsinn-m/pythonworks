#most recursive character 

text="QWERTTWW"

def get_count(ch):

    return text.count(ch)

mosst_frequent_character=max(text,key=get_count)

print(mosst_frequent_character)

least_frequent_character=min(text,key=get_count)

print(least_frequent_character)