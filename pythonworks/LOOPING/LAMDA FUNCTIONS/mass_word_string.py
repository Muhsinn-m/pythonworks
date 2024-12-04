text="this is a simple progtram to find word with words  maximum numbers of character"

words=text.split(" ")

def get_length(w):

    return len(w)

srt_words=sorted(words,key=get_length,reverse=True)

print(srt_words)


text="this is a simple programming question to find word with maximum number with characters"

words=text.split(" ")

def get_count(w):

    return words.count(w)

frequent_word=max(words,key=get_count)

print(frequent_word)