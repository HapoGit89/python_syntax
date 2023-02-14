def print_upper_words(words, letters):   
    for word in words:
        for letter in letters:
            if letter.lower() == word[0].lower():
                print (f"{word.upper()}")

wordz = ["Tom", "dog", "Maine", "banana", "Eating"]

print_upper_words(wordz, {"b", "D"})

