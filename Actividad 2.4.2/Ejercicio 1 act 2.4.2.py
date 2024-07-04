
liviana = 0
normal = 0

print ("Bienvenido a la calculadora de bultos\n 1 - 5 kilos = C. Liviana\n 6 - 10 kilos = C. Normal\n")

try:
    bultos = int(input("Ingrese cuántos bultos: "))
    for x in range(1, bultos + 1):
        pesos = int(input(f"Peso del {x} bulto en Kilos: "))
        if pesos >= 1 and pesos <= 5:
            liviana += 1000
        elif pesos >= 6 and pesos <= 10:
            normal += 2000

    print (f"El total sería de ${liviana + normal} CLP")


except ValueError:
    print("ERROR EN EL PROGRAMA, INTENTE NUEVAMENTE")
