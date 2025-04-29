import random

print("""
╔════════════════════════════╗
║   WELCOME TO BLACKJACK!    ║
╚════════════════════════════╝
""")
deal=0
hand=0
pepo=10

while pepo !=0 and pepo!=1:
    pepo=int(input("Press 1 to play \n 0 to exit \n"))
    if pepo==1:
         while hand <= 21:
               deal=(int(input("1.-Deal card \n 2.-Stop dealing")))
               if deal==1:
                 card=random.randint(1,13)
                 hand+=card
                 
                 print(f"\nYou got a {card} \n your hand is {hand} \n")
               elif deal==2:
                 break
               else:
                 print ("please enter 1 or 2")
            if hand==21:
                print (f"Sheesh you really made it you got {hand}")
            elif hand>21:
             print (f"You lost, your hand is {hand}")
             if hand>0 and hand<21:
                 print (f"You have {hand} in your hand")
    elif pepo==0:
        print("Goodbye")
    else:("Please enter a valid option")


