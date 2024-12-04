text=""
words=text.split(" ")

word_frequency={w:words.count(w) for w in words}

print(max(word_frequency))