Algoritmo contador3
	
	Definir tot, num Como Entero;
	
	tot = 0;
	Escribir Sin Saltar "Ingrese un n�mero";
	leer num;
	
	Mientras num <> 0 Hacer
		
		tot = num + tot;
		Escribir "Total = ", tot;
		Escribir Sin Saltar "Ingrese otro n�mero";
		leer num;
		
		Limpiar Pantalla;
		
		Escribir "Usted puede salir del bucle escribiendo 0";
		
		
	FinMientras
	
	Limpiar Pantalla;
	
FinAlgoritmo
