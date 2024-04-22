#Etapa 1
print ("\nBienvenido al mundo de la programación")
nombre = str(input("Para continuar, ingresa tu nombre: "))

#Etapa 2
print (f"\nBienvenido {nombre}\n")

#Etapa 3
x = int(input("Ingresa un número: "))
print (f"El resultado es: {(x ** 2 + 3 * x + 1)/4}\n")

#Etapa 4
apellido = str(input("Ingresa tu apellido: "))
rut = str(input("Ingresa tu rut: "))
correo = str(input("Ingresa tu correo: "))
telefono = str(input("Ingresa tu número telefónico: "))
print (f"\nNOMBRE:\t\t {nombre.upper() + " " + apellido.upper()}\nRUT:\t\t {rut}\nCORREO:\t\t {correo.upper()}\nTELÉFONO:\t {telefono}\n\n¡Hasta luego!")