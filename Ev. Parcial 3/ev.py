destinos = ["Torres del paine", "Carretera Austral", "Chiloé"]
datosClientes = []

try:
    def registrarReserva (destinos):
        nombreUser = input("Ingrese su nombre: ").lower().capitalize()
        apellidoUser = input("Ingrese su apellido: ").lower().capitalize()
        ciudadUser = input("Ingrese su ciudad de origen: ").lower().capitalize()
        print("Destino del tour, seleccione un destino\n1) Torres del Paine\n2) Carretera Austral\n3) Chiloé")
        while True:
            opc2 = int(input("Opción: "))
            if opc2 >= 1 and opc2 <= 3:
                cantidadUser = int(input("Cantidad de Personas: "))
                cliente = nombreUser + " " + apellidoUser
                datosTodos = f"Cliente: {cliente} | Ciudad de Origen: {ciudadUser} | Tour: {destinos[opc2 - 1]} | Cantidad de Personas: {cantidadUser}"
                return datosTodos
            else:
                print("Ingrese una ciudad correcta.")

    def enlistarReservas(datosClientes):
        if len(datosClientes) == 0:
            print("\nNo hay viajes registrados\n")
        else:
            for i, valor in enumerate(datosClientes):
                print(f"{i + 1}. {valor}")
            print("")    
    
    def imprimirReservas(datosClientes):
        with open("Reservas.txt", 'w', encoding='utf-8') as txt:
            for i, valor in enumerate(datosClientes):
                txt.write(f"{i + 1}. {valor}\n")

    while True:
        print("\n         ---MENÚ---\n1) Registrar reserva\n2) Listar todas las reservas\n3) Imprimir Detalle de reservas por destino\n4) Salir del programa\n")
        opc = int(input("Opción: ")) 

        if opc == 1:
            datosClientes.append(registrarReserva(destinos))
            print("\nReserva registrada con éxito\n")
        elif opc == 2:
            enlistarReservas(datosClientes)
        elif opc == 3:
            imprimirReservas(datosClientes)
        elif opc == 4:
            print("¿Desea salir del programa?\n1) Si\n2) No")
            opc = int(input("Opción: "))
            if opc == 1:
                print("Hasta luego")
                break
            elif not opc == 2:
                print("Seleccione una opción válida")
        else:
            print("Seleccione una opción válida")
                
except:
    print("Error en el programa, comuníquese con el trabajador")