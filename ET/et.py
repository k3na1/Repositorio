import random
import time
import statistics as stat

def asignarSueldo(trabajadores):
    sueldos = {}
    for trabajador in trabajadores:
        sueldos[trabajador] = random.randint(300000,2500000)
    return sueldos

def clasificadorSueldos(diccionario):
    sueldosTrabajador = diccionario.values()
    listaSueldos = list(sueldosTrabajador)
    contador1 = 0
    contador2 = 0
    contador3 = 0
    for sueldo in listaSueldos:
        if sueldo < 800000:
            contador1 += 1
        elif sueldo > 800000 and sueldo < 2000000:
            contador2 += 1
        elif sueldo > 2000000:
            contador3 += 1
    print(f"\nSueldos menores a $800.000 CLP | TOTAL: {contador1}\nNombre Empleado        Sueldo" )
    for nombre, valor in diccionario.items():
        if valor < 800000:
            print(f"{nombre}            ${valor}")
    print("")
    print(f"Sueldos entre $800.000 CLP y $2.000.000 | TOTAL: {contador2}\nNombre Empleado        Sueldo" )
    for nombre, valor in diccionario.items():
        if valor > 800000 and valor < 2000000:
            print(f"{nombre}            ${valor}")
    print("")
    print(f"Sueldos superiores de $2.000.000 | TOTAL: {contador3}\nNombre Empleado        Sueldo" )
    for nombre, valor in diccionario.items():
        if valor > 2000000:
            print(f"{nombre}            ${valor}")
    print("")

    print(f"TOTAL SUELDOS: ${sum(listaSueldos)}")

def estadisticas(diccionario):
    sueldos = diccionario.values()
    listaSueldos = list(sueldos)
    sueldoMaximo = max(listaSueldos)
    sueldoMinimo = min(listaSueldos)
    for nombre, valor in diccionario.items():
        if valor == sueldoMaximo:
            print(f"\nSueldo más alto: {nombre}: ${sueldoMaximo}")
        if valor == sueldoMinimo:
            print(f"Sueldo más bajo: {nombre}: ${sueldoMinimo}")
    print(f"Promedio de sueldo: ${sum(listaSueldos) / len(listaSueldos)}")
    print(f"Media geométrica: ${round(stat.geometric_mean(listaSueldos),1)}\n")
  
def descuentoSalud(diccionario):
    sueldos = diccionario.values()
    listaSueldos = list(sueldos)
    listaTrabajadores = list(diccionario.keys())
    diccionarioDescuento = {}
    for sueldo in listaSueldos:
        sueldoTotal = sueldo * 0.07
        for trabajador in listaTrabajadores:
            diccionarioDescuento[trabajador] = round(sueldoTotal)
    return diccionarioDescuento

def descuentoSaludAFP(diccionario):
    sueldos = diccionario.values()
    listaSueldos = list(sueldos)
    listaTrabajadores = list(diccionario.keys())
    diccionarioDescuento = {}
    for sueldo in listaSueldos:
        sueldoTotal = sueldo * 0.12
        for trabajador in listaTrabajadores:
            diccionarioDescuento[trabajador] = round(sueldoTotal)
    return diccionarioDescuento


trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
diccionarioSueldos = {}
flag = True


while flag == True:
    try:
        print ("    ----MENÚ----\n1) Asignar sueldos aleatorios\n2) Clasificar sueldos\n3) Ver Estadísticas\n4) Reporte de sueldos\n5) Salir")
        opcion = int(input("Opción: "))
        if opcion == 1:
            print("Generando sueldos...")
            diccionarioSueldos = asignarSueldo(trabajadores)
            time.sleep(0.5)
            print("Sueldos generados exitosamente")
        elif opcion == 2:
            if diccionarioSueldos == {}:
                print("Primero genere los sueldos antes de continuar (OPCIÓN 1)")
            else:
                clasificadorSueldos(diccionarioSueldos)
        elif opcion == 3:
            if diccionarioSueldos == {}:
                print("Primero genere los sueldos antes de continuar (OPCIÓN 1)")
            else:
                estadisticas(diccionarioSueldos)
        elif opcion == 4:
            if diccionarioSueldos == {}:
                print("Primero genere los sueldos antes de continuar (OPCIÓN 1)")
            else:
                print("Nombre empleado  Sueldo base     Descuento Salud     Descuento AFP   Sueldo liquido")
                datos = []
                for nombre, valor in diccionarioSueldos.items():
                    datos.append(f"{nombre},{valor},{round(valor * 0.07)},{round(valor * 0.12)},{round(valor - ((valor * 0.07) + (valor * 0.12)))}")
                    print(f"{nombre}   {valor}  {round(valor * 0.07)}  {round(valor * 0.12)}  {round(valor - ((valor * 0.07) + (valor * 0.12)))}")
                print("\nArchivo CSV generado")
                with open("Sueldos.csv", 'w', encoding='utf-8') as archivo:
                    archivo.write(f"NombreEmpleado,SueldoBase,DescuentoSalud,DescuentoAFP,SueldoLiquido\n")
                    for i, dato in enumerate(datos):
                        archivo.write(f"{dato}\n")
        elif opcion == 5:
            print("Finalizando programa...\nDesarrollado por Francisco Aránguiz\nRUT 21.321.123-4")
            time.sleep(2)
        else:
            print("Seleccione una opción válida")
                
    except:
        print("ERROR. VERIFIQUE LOS DATOS Y SI EL PROBLEMA PERSISTE CONTACTAR CON UN SUPERVISOR")
