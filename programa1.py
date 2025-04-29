user_entered_number=0
evens=[]
odds=[]

user_entered_number=(int(input("Enter a number: ")))
if user_entered_number % 2 ==0:
    print (f"{user_entered_number} is even")
elif user_entered_number % 2 !=0:
    print (f"{user_entered_number} is odd")
else:
    print("please enter a valid option")

for i in range (user_entered_number+1):
  if i % 2 == 0:
   evens.insert (-1, i)
  else:
   odds.insert (-1, i)

print(f"The evens are {evens}")
print(f"The odds are {odds}")



