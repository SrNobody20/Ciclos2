peluches = ["roshi","conejito","aguacate"]

print (peluches)

opcion=0
print("Pelicheria ")
print("...................")
print("1. Agregar productos a la bodega ")
print("2. Ver productos en bodega ")
print("3. Obtener valor del inventario")
print("4. Ver productos mas vendidos")
print("5. SALIR")

while(opcion!=5):
    opcion=int(input("Digite un numero: "))

    if opcion==1:
     print ("Usted esta en la opcion 1")
    elif opcion==2:
       print("Usted esta en la opcion 2")
    elif opcion==3:
       print("Usted esta en la opcion 3")
    elif opcion==4:
       print("Usted esta en la opcion 4")
    elif opcion==5:
       print("SALIR")

print("sali del ciclo")
