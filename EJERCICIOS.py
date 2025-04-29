import random
user_entered_number=pepo
evens=[]
odds=[]
while user_entered_number!=int:

user_entered_number=int(input("Enter a number: "))
if user_entered_number % 2 == 0:
    evens.insert (user_entered_number)
elif user_entered_number % 2 != 0:
    odds.insert (user_entered_number)
    