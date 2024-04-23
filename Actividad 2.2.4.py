# Ejercicio 1
# Respuesta:
nom = input ("Ingrese nombre empleado: ")
rut = input ("Ingrese rut empleado: ")
horasTrabajadas = int(input ("Ingrese las horas trabajadas: "))
valorHora = int(input("Ingrese el valor hora del empleado: "))
colacion = int(5500)
movilizacion = int(3000)
resultado = (valorHora * horasTrabajadas)+colacion+movilizacion

print(f"-----LIQUIDACIÓN EMPLEADO----")
print(f"NOMBRE EMPLEADO: {nom}")
print(f"RUT EMPLEADO: {rut}")
print(f"MOVILIZACIÓN: {movilizacion}")
print(f"ALIMENTACIÓN: {colacion}")
print(f"PAGO A EMPLEADO: {resultado}")

# Ejercicio 2
# Respuesta:
# La opciones correctas son: opcion1, opcion3, opcion5

# Ejercicio 3
# Respuesta:
posicionA = "X"
posicionB = ""
posicionC = ""
posicionD = ""
posicionE = "X"
posicionF = ""
posicionG = ""
posicionH = ""
posicionI = "X"
print("")
print("\t\t|\t\t |\t")
print(f"\t{posicionA}\t|\t{posicionB}\t |\t{posicionC}")
print("\t\t|\t\t |\t")
print("----------------------------------------------------")
print("\t\t|\t\t |\t")
print(f"\t{posicionD}\t|\t{posicionE}\t |\t{posicionF}")
print("\t\t|\t\t |\t")
print("----------------------------------------------------")
print("\t\t|\t\t |\t")
print(f"\t{posicionG}\t|\t{posicionH}\t |\t{posicionI}")
print("\t\t|\t\t |\t")
print("")

# Ejercicio 4
# Respuesta:
print("Ingresar los datos de la venta")
cliente = input("Ingrese el nombre del cliente: ")
precio1 = int(input("Ingrese el precio del producto1: "))
cantidad1 = int(input("Ingrese la cantidad del producto1: ")) 
precio2 = int(input("Ingrese el precio del producto2: "))
cantidad2 = int(input("Ingrese la cantidad del producto2: "))
precio3 = int(input("Ingrese el precio del producto3: "))
cantidad3 = int(input("Ingrese la cantidad del producto3: "))
descuento = int(input("Ingrese el descuento: "))

total_bruto = (precio1 * cantidad1) + (precio2 * cantidad2) + (precio2 *
cantidad2)
precio_con_descuento = round(total_bruto - (total_bruto * descuento/
100))
iva = round(float(precio_con_descuento * 0.19))
print("")
print(f"Cliente: \t{cliente}")
print(f"Total bruto: \t${total_bruto}")
print (f"Total desc.: \t${precio_con_descuento}")
print(f"Iva: \t\t${iva}")
print(f"Total: \t\t${precio_con_descuento + iva}")

# Ejercicio 5
# Respuesta:
linea1 = (" ___ |\________/)")
linea18 =(" [_,_]) \ / \|")
linea11 =(" /|=T=|] / __ __\\")
linea13 =(" |\ ' // |_ 9 p ]\\")
linea15 =(" ||'-'/--. / /\\ =| \|\\ \\")
linea16 =(" /|| <\/> |\ | '._, @ @)<_)")
linea21 =(" | |\ | | \.__/(_;_)")
linea31 =(" | . H | | : '='|")
linea6 =(" | | _H__/ _| : |")
linea7 =(" \ '.__ \ / ; ';")
linea19 =(" __'-._(_}==.' : ;")
linea71 =(" (___| /-' | :. :")
linea371 =(" [.-' \ | \ \ ; :")
linea2 =(" .-' | | | | ':")
linea22 =(" / |==| \ \ / \_")
linea661 =(" / [ | '._\_ -._ \\")
linea517 =(" / \__) __.- \ \ )\\")
linea81 =("/ | /.' >>)")
linea61 =("| \ |\ |")
linea414 =("| .' '-. | \ /")
linea651 =("| / / / / /")
linea51 =(" | /")
linea41 =("")

