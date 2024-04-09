Algoritmo promedioAlumnos
	
	definir nota_1, nota_2, nota_3, total como real; 	// Definición de variables
	
	Escribir "Ingrese 3 notas como enteros de su estudiante para promediar"; 		// Consultar al usuario y guardar los datos obtenidos en dichas variables
	Escribir Sin Saltar "Nota 1";
	Leer nota_1;
	Escribir Sin Saltar "Nota 2";												
	leer nota_2;
	Escribir Sin Saltar "Nota 3";
	leer nota_3;
	
	total = redon((nota_1 + nota_2 + nota_3) / 3);					// Hacer cálculo para sacar promedio de los 3 datos otorgados como enteros usando "redon" para reducir decimal
	
	si total >= 40 Entonces										// Consultar si el promedio obtenido es superior a 40 para recibir el mensaje de apruebo
		Escribir "Su estudiante aprobó con un ", total;		
	SiNo
		Si total <= 40 Entonces									// Consultar si el promedio obtenido es inferior a 40 para recibir el mensaje de repruebo
			Escribir "Su estudiante reprobó con un ", total;
		FinSi
	FinSi

FinAlgoritmo 
