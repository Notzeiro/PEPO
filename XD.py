import random

number_to_guess= random.randint(1, 51)
user_guess=1546413784592364923847298

while number_to_guess!=user_guess:
    user_guess=(int(input("Enter a number: ")))
    if number_to_guess>user_guess:
        print ("The number is greater, try again")
    elif number_to_guess<user_guess:
        print ("The number is smaller, try again")

print(f"Congratulations, the number was {number_to_guess}, and you guessed it")







