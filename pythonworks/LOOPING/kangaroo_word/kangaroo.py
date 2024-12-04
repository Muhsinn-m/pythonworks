source_word="CHICKENN"

target_word="HEN"

character_count={ch:source_word.count(ch) for ch in source_word}

is_kangaro=True

for ch in target_word:

    if ch in character_count and character_count.get(ch)>0:

        character_count[ch]-=1

    else:    
        is_kangaro=False

        break
    
print(is_kangaro)



