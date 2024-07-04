
def division(num1, num2):
    try:
        total = 0
        total = num1 / num2
        return total
    except ZeroDivisionError:
        return "Error de división. No se puede dividir por cero" 

while True:
    try:
        print ("Ingrese dos números")
        dato1 = int(input("Ingrese un dato: "))
        dato2 = int(input("Ingrese un segundo dato: "))
        print(division(dato1,dato2))
    except ValueError:
        print("Error de valor, ingrese uno correcto")
