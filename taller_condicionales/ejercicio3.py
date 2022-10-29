"""
Escribir un programa que reciba por teclado la edad de 3 personas ingresadas por el usuario y 
determinar la edad del más joven entre ellos.
"""
try:
    edad1 = int(input("Ingrese la edad 1: "))
    edad2 = int(input("Ingrese la edad 2: "))
    edad3 = int(input("Ingrese la edad 3: "))

    if edad1 <= edad2 and edad1 <= edad3:
        print("El más joven es el primero")
    elif edad2 <= edad1 and edad2 <= edad3:
        print("El más joven es el segundo")
    else:
        print("El más joven es el tercero")

except ValueError:

    print("Edades no enteras")