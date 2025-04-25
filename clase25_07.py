kaiser=0
kast=0
merluzo_pastero=0


vote=2
while vote != 0:
    vote=(int(input(" 1.-Kaiser \n 2.-Kast \n 3.-Merluzo_pastero \n\n 0.- To terminate the votation\n\n Enter your vote: ")))
    if vote==1:
        kaiser+=1
    elif vote==2:
        kast+=1
    elif vote==3:
        merluzo_pastero+=1
    elif vote==0:
        continue
    else: print ("Error, please enter a valid selection")


locos = [kaiser , kast , merluzo_pastero]
winner= max(locos)
winnersname=""
if winner==kaiser:
    winnersname="Kaiser"
elif winner==kast:
    winnersname="Kast"
elif winner==merluzo_pastero:
    winnersname="Merluzini callampini"

for x in locos:
   if x==winner:
    
    print (f"There is a tie with winner and {x}")

votestotal=kaiser+kast+merluzo_pastero

print(f"the total votes are: {votestotal}\n \n The winner is {winnersname}")
