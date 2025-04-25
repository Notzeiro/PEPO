
total=0
product=1
while product !=0:
    print("WELCOME TO NOTZEIRO`S STORE \n to exit press 0 \n product list: \n 1. Milk $2000 \n 2. Bread $1000\n 3. Eggs $7000\n 4. Butter $8000\n 5. Cheese $20000 \n 6. Ham $20300")
    product=int(input("Enter the product you want to add: "))
    if product==1:
        print ("You added Milk")
        total +=2000
    elif product==2:
        print ("You added bread")
        total +=1000
    elif product==3:
        print ("You added eggs")
        total +=7000
    elif product==4:
        print ("You added butter")
        total +=8000
    elif product==5:
        print ("You added cheese")
        total +=20000
    elif product==6:
        print ("You added ham")
        total +=20300

print(f"your total is: {total} " )