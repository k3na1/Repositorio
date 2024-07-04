
liviana = 0
normal = 0
vuelta = 1

print ("Bienvenido a la calculadora de bultos\n 1 - 5 kilos = C. Liviana\n 6 - 10 kilos = C. Normal\n")

try:
    bultos = int(input("Ingrese cuántos bultos: "))
    while vuelta <= bultos:
        vuelta += 1
        pesos = int(input(f"Peso del {vuelta - 1} bulto en Kilos: "))
        if pesos >= 1 and pesos <= 5:
            liviana += 1000
        elif pesos >= 6 and pesos <= 10:
            normal += 2000

    print (f"El total sería de ${liviana + normal} CLP")


except ValueError:
    print("ERROR EN EL PROGRAMA, INTENTE NUEVAMENTE")
