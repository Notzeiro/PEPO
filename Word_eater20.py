word_without_vowels = ""
user_word=str(input("enter a word: "))
user_word = user_word.upper()
for letter in user_word:
    if letter not in {"A" , "I" , "E" , "O" , "U"}:
     word_without_vowels += letter 
    

print (word_without_vowels)