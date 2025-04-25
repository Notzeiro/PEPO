import random
print("""
╔════════════════════════════╗
║   WELCOME TO BLACKJACK!   ║
╚════════════════════════════╝
""")
deal=0
hand=0
pepo=10
pepo=int(input("Press 1 to play \n 0 to exit"))
if pepo==1:
        while hand <= 21:
            deal=(int(input("1.-Deal card \n 2.-Stop ")))
        if deal==1:
            card=random.randint(1,13)
            hand+=card
            print(f"You got a {card} \n your hand is {hand}")
elif pepo==0:
 print("goodbye") break

