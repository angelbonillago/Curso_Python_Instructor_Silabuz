"""
Ejercicio 1
Escribir un programa que reciba por teclado dos números y un operador matemático(+,-,*,/). 
Realice la operación correspondiente e imprima el resultado. 
En caso el operador sea distinto a los mencionados imprimir "Operador no aceptado"
"""

try:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    operador = input("Ingrese el operador")

    if operador == "+":
        print(num1+num2)
    elif operador == "-":
        print(num1-num2)
    elif operador == "*":
        print(num1*num2)
    elif operador == "/":
        print(num1/num2)
    else:
        print("Operador no aceptado")

except ValueError:

    print("Numero u operando incorrecto")
