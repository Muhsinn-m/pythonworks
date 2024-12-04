text=["orange","apple","strowberry","mango"]

longest=max([len(w)for w in text])

longest_words=[w for w in text if len (w)==longest]

print(longest_words)


