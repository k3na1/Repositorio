# Ejercicio 1
# Respuesta:
rut = input ("Ingrese rut apoderado: ")
nomAlum = input("Ingrese el nombre del alumno: ")
curso = input("Ingrese curso al cual el alumno debe matricularse: ")
matricula = int(25000)
mensualidad = int(30000)
resultadoAnual = (mensualidad*10)+matricula

print(f"-----Detalle Anualidad Colegio----")
print(f"VALOR MATRÍCULA: {matricula}")
print(f"VALOR MENSUALIDAD: {mensualidad}")
print(f"VALOR TOTAL A PAGAR: {resultadoAnual}")
print(f"NOMBRE ALUMNO: {nomAlum}")
print(f"RUT APODERADO: {rut}")
print(f"CURSO MATRICULADO: {curso}")
print("\n")

# Se ordena de forma en la que se quiere el orden de salida y el orden 
# de la solicitud de variables.


# Ejercicio 2
# Respuesta:
producto = input ("Ingrese el nombre del producto: ")
valorProducto = int(input("Ingrese el valor del producto: "))
valorNeto = float(0.81)
valorSinIva = float(valorProducto * valorNeto)
print(f"-----Detalle producto----")
print(f"NOMBRE PRODUCTO: {producto}")
print(f"VALOR PRODUCTO: {valorProducto}")
print(f"VALOR PRODUCTO SIN IVA: {valorSinIva}")

# ¿Por qué se debe ocupar tipo de dato Float para calcular el IVA?
# El tipo de variable Float sirve para almacenar datos numéricos de tipo decimal, 
# si usamos Int (Integer), solo serán datos numéricos de tipo entero y el programa
# dará error.

# Ejercicio 3    
# La secuencia es: 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610