try: 
    comuna=(int(input("1.-La florida \n 2.-La pintana \n 3.-Puente alto \n 4.-San Joaquin \n Indique su comuna: ")))
    descuento=0
    arancel=200000
    personas_con=(int(input("Cuantas personas viven en tu casa?(Incluyete a ti mismo): ")))
    if personas_con==1:
     descuento+=2
    elif personas_con>=2 or personas_con<=4:
     descuento+=3
    elif personas_con>5:
     descuento+=4

    if comuna==1:
     descuento+=20
    elif comuna==2:
     descuento+=30
    elif comuna==3:
     descuento+=25
    elif comuna==4:
     descuento+=15

    precio_final=int(arancel-(arancel*descuento/100))

    print(f"Su precio final es de {precio_final} \n el descuento aplicado fue del {descuento}%")
except ValueError: print("Respuesta invalida, por favor ingrese lo solicitado") 
except: print ("Lo sentimos, algo salio mal...")







