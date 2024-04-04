Algoritmo contador2
	
	definir contador, cuadrado Como Entero;
	definir limite Como Entero;
	contador = 1;	
	
	Escribir Sin Saltar "Ingrese un numero";
	leer limite;
	
	Mientras contador <= limite Hacer
		
		cuadrado = contador * contador;
		Escribir contador, " al cuadrado es ", cuadrado;
		contador = contador + 1;
		
	FinMientras
	
	
FinAlgoritmo
