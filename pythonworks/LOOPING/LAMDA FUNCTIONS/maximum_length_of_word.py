words=["hello","hai","morning","test","apple"]

def get_length(word):

    return len(word)
   
print(max(words,key=get_length))


#find the largest words in the text

text="this is a simple programming launguage in the coding section"

words=text.split(" ")

def get_length(w):

    return len(w)

print(max(words,key=get_length))

