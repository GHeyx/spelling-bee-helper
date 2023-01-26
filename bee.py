import re

def find_words(letters):
    words = []

    with open('robust.txt') as file:
        text = file.read()
    
    words_in_text = text.split()

    letters_set = set(letters)

    first_letter = letters[0]

    for word in words_in_text:
    # check if the word is long enough and contains only the given letters
        if (set(word).issubset(letters_set) and first_letter in word):
            words.append(word)

    return words        
    
    
todays_letters = input('What are todays letters? Note: Let the first letter be the center letter.')
        
words = find_words(todays_letters)
#print(sorted(words))
[print(i) for i in sorted(words)]
