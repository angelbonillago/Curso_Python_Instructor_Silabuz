"""
# Ejercicio 2

Una empresa ha decidido dar una bonificación del 5% al empleado cuyo tiempo de servicio sea superior a 3 años.

Escribir un programa que reciba por teclado el monto del salario y los años de servicio e imprima la 
cantidad neta de la bonificación.

"""
try:
    salario = float(input("Ingrese el salario: "))
    tiempo = int(input("Ingrese la cantidad de años: "))

    if tiempo > 3:
        print("La bonificación es: ", (salario+(salario * 0.05)))
    else:
        print("No existe bonificación")

except ValueError:

    print("cantidades no validas")