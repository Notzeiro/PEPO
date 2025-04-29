op=-1
amount_of_numbers_added=0
add=0
while op==-1:
    num=(int(input("To exit press 0 \n Enter a number: ")))
    add+=num
    amount_of_numbers_added+=1
    if num==0:
     break

print (f"The amount of numbers entered are {amount_of_numbers_added} \n The total add of them is {add}")


