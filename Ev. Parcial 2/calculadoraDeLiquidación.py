
#Solicitar datos trabajador
def verificador (nombre, sueldo, hTrabajadas):
    valido = bool
    if len(nombre) > 30:
        print ("ERROR: NOMBRE DE TRABAJADOR MUY LARGO. INGRESE UN NOMBRE MENOR DE 30 CARÁCTERES")
        valido = False
    elif nombre == "":
        print ("ERROR: NOMBRE DE TRABAJADOR VACÍO. INGRESE UN NOMBRE PARA CONTINUAR")
        valido = False
    elif sueldo <= 0 or hTrabajadas <= 0:
        print ("ERROR: SUELDO O HORAS TRABAJADAS EXTRAS NO VÁLIDAS. INGRESE DATOS NUEVOS")
        valido = False
    else:
        valido = True
    return valido
def calculoHoras (sueldo):
    total = round((sueldo / 30) * 28 / 180, 1)
    return total

flag = True

print ("\n\tCÁLCULO DE LIQUIDACIÓN\n")

while flag == True:
    try:
        userName = str(input("Ingrese el nombre del trabajador: ")).upper()
        userSueldo = int(input("Ingrese el sueldo del trabajador: "))
        userHTrabajadas = int(input("Ingrese las horas trabajadas EXTRAS en el mes: "))
    except:
        print ("ERROR: DATOS INGRESADOS NO VÁLIDOS. INGRESE DATOS NUEVOS.")
    else:
# Verificar datos válidos. Si es válido, calcular sueldo
        if verificador(userName, userSueldo, userHTrabajadas) == True:
            flag = False

            horasPagadas = calculoHoras(userSueldo)
            PagoXHorasExtra = round((calculoHoras(userSueldo) * 1.5) , 1)
            PagoXHorasExtraT = round((calculoHoras(userSueldo) * 1.5) * userHTrabajadas, 1)
            sueldoHExtra = (PagoXHorasExtraT * userHTrabajadas) + userSueldo
            descuentoFonasa = round(sueldoHExtra * 0.07 , 1)
            descuentoAFP = round(sueldoHExtra * 0.10 , 1)
            descuentoSS = round(descuentoFonasa + descuentoAFP)
            sueldoTotal = round(sueldoHExtra - descuentoSS , 1)

            print(
                f"""
                LIQUIDACIÓN

        NOMBRE TRABAJADOR:      {userName}
        SUELDO BASE:            ${'{:,}'.format(userSueldo)}
        PAGO POR HORA EXTRA:    ${'{:,}'.format(PagoXHorasExtra)}
        PAGO POR HORAS EXTRA:   ${'{:,}'.format(PagoXHorasExtraT)}
        TOTAL INGRESOS:         ${'{:,}'.format(sueldoHExtra)}
        DESCUENTO S. SOCIAL:    ${'{:,}'.format(descuentoSS)}
        SUELDO NETO:            ${'{:,}'.format(sueldoTotal)}
                
                """
                )
            
            with open (f"liquidación_{'_'.join(userName.split())}.txt","w", encoding='utf-8') as liquidación:
                liquidación.write (    
               f"""
                LIQUIDACIÓN

        NOMBRE TRABAJADOR:      {userName}
        SUELDO BASE:            ${'{:,}'.format(userSueldo)}
        PAGO POR HORA EXTRA:    ${'{:,}'.format(PagoXHorasExtra)}
        PAGO POR HORAS EXTRA:   ${'{:,}'.format(PagoXHorasExtraT)}
        TOTAL INGRESOS:         ${'{:,}'.format(sueldoHExtra)}
        DESCUENTO FONASA:       ${'{:,}'.format(descuentoFonasa)}
        DESCUENTO AFP:          ${'{:,}'.format(descuentoAFP)}
        SUELDO NETO:            ${'{:,}'.format(sueldoTotal)}
                
                """

                )


