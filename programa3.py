from random import randint
num=int(input("Enter a number: "))
num2=randint(2,8)
num*= num2

if num>50:
    print (f"congrats, you made it your number was multiplied by {num2} so you got {num}")
else:
    print (f"You didnt reach over 50, you number was multiplied by {num2} and got {num}")