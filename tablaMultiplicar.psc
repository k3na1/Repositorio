Algoritmo tablaMultiplicar
	
	Definir num, numAumento, total Como Entero; 					//Se define las variables para realizar la tabla como enteros
	Definir op Como caracter;									//Se define la variable "op" como caracter para usarla si el usuario desea hacer otra tabla
	
	
	Repetir 		//Entra al bucle
		Limpiar Pantalla;		
		Escribir "Escribe un número entero para hacer la tabla de multiplicar";
		leer num;																	//Pregunta al usuario el numero entero para realizar la tabla
		
		para numAumento <- 1 hasta 10 Con Paso 1 Hacer							//La variable numAumento se le asigna el valor 1 para que con cada bucle se le sume de a 1 hasta 10
			total = num * numAumento;												//Se multiplica el numero dado por el numero en aumento y guardarlo en la variable "total"
			Esperar 50 Milisegundos;;
			Escribir num, " * ", numAumento, " = ", total;							//Escribe en la consola el resultado de la multiplicación
		FinPara
		
		Escribir "¿Desea hacer otra tabla? (si/no)";				
		leer op;																	//Pregunta al usuario si desea usar otra acción y guardarlo en la variable "op"
		
		Si op == Minusculas("no") o op == Mayusculas("no") Entonces
			Limpiar Pantalla;
			Escribir "¡Hasta luego!"; 
		FinSi																		//Si el usuario escribe "no", se limpia la pantalla, la consola escribe "Hasta luego"
		
	Hasta Que op == Minusculas("no") o op == Mayusculas("no");						//Si el usuario guarda en la variable "op" el caracter "no" el bucle termina. Si no es asì, vuelve hasta la linea 7
	
	
	
	
FinAlgoritmo
