Algoritmo sin_titulo
	
	definir numeroPorAdivinar Como Entero
	Definir numeroUsuario como entero
	definir intentos Como Entero
	Definir intentosLimite Como Entero
	
	numeroPorAdivinar = azar(100)
	Escribir numeroPorAdivinar
	intentosLimite = 0
	intentos = 5
	
	
	Escribir "�Adivina el n�mero! Tienes 5 intentos"
	leer numeroUsuario
	Mientras no numeroPorAdivinar = numeroUsuario y intentosLimite <> intentos Hacer
		intentos = intentos - 1
		Si numeroUsuario < numeroPorAdivinar Entonces
			
			Escribir "El n�mero por adivinar es mas alto, te quedan ", intentos, " intentos"
		SiNo
			si numeroUsuario > numeroPorAdivinar
				
				Escribir "El n�mero por adivinar es mas bajo te quedan ", intentos, " intentos"
			FinSi
		FinSi
		leer numeroUsuario
	FinMientras
	
	
	
	si numeroUsuario == numeroPorAdivinar Entonces
		Escribir "�Felicidades! Usted adivin� el n�mero ", numeroPorAdivinar, "!"
	SiNo
		Escribir "�Una l�stima! No pudiste adivinar el n�mero ", numeroPorAdivinar
	FinSi
	
	
FinAlgoritmo