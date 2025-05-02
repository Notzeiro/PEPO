import time
import random
goal=-1
while goal<0:
    goal=(int(input("Set the goal, 30 is standard for ludo: ")))
    if goal==0 or goal<0:
        print("please enter a valid option")

turn=random.randint(0,11)
p1=(input("Enter player 1 name: "))
p2=(input("Enter player 2 name: "))
p1_score=0
p2_score=0
scores=[p1_score, p2_score]
players_names=[p1, p2]

while p1_score<goal or p2_score<goal:
    if p1_score>=goal or p2_score>=goal:
        break

    if turn % 2==0:
        p1dice=random.randint(1,7)
        print(p1 , "'s turn")
        turn+=1
        p1_score+=p1dice
        print(f"{p1} got a {p1dice} so hes at {p1_score} block")
    else:
        p2dice=random.randint(1,7)
        print(p2 , "'s turn")
        turn+=1
        p2_score+=p2dice
        print(f"{p2} got a {p2dice} so hes at {p2_score} block")


winner=players_names[(max(scores))]



print(f"the winner is {winner}")




    
