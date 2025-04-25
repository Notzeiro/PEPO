user_word=str(input("Enter a word "))
user_word = user_word.upper()
for letter in user_word:
  if letter in {"A" , "E" , "I" , "O" , "U" }:
    continue
  else: 
       print(letter)
    

odds = [x for x in squares if x % 2 != 0 ]