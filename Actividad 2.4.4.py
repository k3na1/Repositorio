totalIngresos = 0

try: 
    cantPasajes = int(input("Ingrese la cantidad de pasajes que desea comprar: "))
    for x in range(0, cantPasajes):
        precio = int(input(f"Ingrese el precio del {x + 1} pasaje: "))
        totalIngresos += precio
    
    print(f"El valor total es de ${totalIngresos} CLP")

except ValueError:
    print("Error en el programa. Ingrese un valor válido")
    