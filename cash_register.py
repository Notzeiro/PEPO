users=["user1", "user2", "user3"]
passwords=[1234,4321,1111]
a=True
while a==True:
    selected_user=(input("Enter user: "))
    if selected_user in users:
     momo=users.index(selected_user)
     password_try=int(input(f"Enter {selected_user}'s password: "))
     if password_try==passwords[momo]:
       print("yes")
     else: print("incorrect")

    else: 
     print ("User misspelled or non existent, please try again")



