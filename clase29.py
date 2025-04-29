# aux=0
# while (aux !=3):
#     print ("1.-item1 $1000 \n 2.- item2 $500 \n 3.- Salir \n")
#     aux=int(input())
#     if (aux==1):
#         print()
        

edad=-1
while (edad<0 or edad>100):
    edad=int(input("ingrese edad: "))
    if (edad<0 or edad>100):
        print("editar, edad fuera de rango [0 , 100]")
print ("edad ingresada exitosamente")