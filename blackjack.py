import random


print("""
╔════════════════════════════╗
║   WELCOME TO BLACKJACK!    ║
╚════════════════════════════╝
""")
deal=0
hand=0
pepo=10


try: 
     
     pepo=int(input("Press 1 to play \n 0 to exit \n"))
     if pepo==1:
        try:
            while hand <= 21:
               deal=(int(input("1.-Deal card \n 2.-Stop dealing \n ")))
               if deal==1:
                 card=random.randint(1,13)
                 hand+=card
                 
                 print(f"You got a {card} \n your hand is {hand}")
               elif deal==2:
                 break
               else:
                 print ("please enter 1 or 2")
             


        except ValueError: print ("Enter a valid option please")
        except:print ("Sorry.. Something went wrong")
     
     
     
     elif pepo==0:
        print("goodbye")
     else:
        print("Please enter 0 or 1")
        
except ValueError: 
   print ("Enter a valid option please")
   
except:
   print ("Sorry.. Something went wrong")
   
 

  

