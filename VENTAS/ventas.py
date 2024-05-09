with open("ventas.txt", 'r') as fichero:
    panCiabattaVentas = []
    pieDeLimonVentas = []
    cafeVentas = []
    teVentas = []
    alfajorVentas = []

    for linea, datos in enumerate(fichero):
        if linea == 0:
            # Divide la línea en una lista de números y conviértelos a enteros
            numeros = [int(numero) for numero in datos.strip().split(',')]
            
            # Agrega la lista de números al array panCiabatta
            panCiabattaVentas.extend(numeros)
        if linea == 1:
            numeros = [int(numero) for numero in datos.strip().split(',')]
            pieDeLimonVentas.extend(numeros)
        
        if linea == 2:
            numeros = [int(numero) for numero in datos.strip().split(',')]
            cafeVentas.extend(numeros)

        if linea == 3:
            numeros = [int(numero) for numero in datos.strip().split(',')]
            teVentas.extend(numeros)
        
        if linea == 4:
            numeros = [int(numero) for numero in datos.strip().split(',')]
            alfajorVentas.extend(numeros)

totalCiabatta = sum(panCiabattaVentas)
totalLimon = sum(pieDeLimonVentas)
totalCafe = sum(cafeVentas)
totalTe = sum(teVentas)
totalAlfajor = sum(alfajorVentas)

print ("------TOTAL DE VENTAS------")
print (f"PAN DE CIABATTA\tTOTAL: {totalCiabatta}\t PROMEDIO VENTAS: {totalCiabatta / 4}")
print (f"PIE DE LIMON\tTOTAL: {totalLimon}\t PROMEDIO VENTAS: {totalLimon / 4}")
print (f"CAFÉ\t\tTOTAL: {totalCiabatta}\t PROMEDIO VENTAS: {totalCafe / 4}")
print (f"TÉ\t\tTOTAL: {totalCiabatta}\t PROMEDIO VENTAS: {totalTe / 4}")
print (f"ALFAJOR\t\tTOTAL: {totalCiabatta}\t PROMEDIO VENTAS: {totalAlfajor / 4}")

with open("informe_ventas.txt", "w", encoding='utf-8') as informe:
    # Escribimos el encabezado del informe
    informe.write("Informe de Ventas - Cafetería de Grano\n\n")
    informe.write("\t\t\t\tLUNES\tMARTES\tMIÉRCOLES\tJUEVES\t\n")
    informe.write("PAN CIABATTA\t50\t\t30\t\t20\t\t\t10\n")
    informe.write("PIE DE LIMON\t40\t\t25\t\t15\t\t\t8\n")
    informe.write("CAFÉ\t\t\t60\t\t35\t\t25\t\t\t12\n")
    informe.write("TÉ\t\t\t\t45\t\t28\t\t18\t\t\t9\n")
    informe.write("ALFAJOR\t\t\t55\t\t32\t\t22\t\t\t11\n\n")
    informe.write(f"TOTAL\t\t\t{50+40+60+45+55}\t\t{30+25+35+28+32}\t\t{20+15+25+18+22}\t\t\t{10+8+12+9+11}\n")

