"""
Ejercicio 5
Dado el diccionario que almacena la talla de algunas personas 
{'Marcelo': 1.80, 'José':1.50, 'Oscar':1.70, 'Jorge': 1.40}, escriba un programa que dado un nombre ingresado 
por el usuario imprime la talla.

Ejemplo:

Ingrese un nombre: Marcelo

Salida: 1.80
"""

diccionario_tallas= {'Marcelo': 1.80, 'José':1.50, 'Oscar':1.70, 'Jorge': 1.40}

print("De este diccionario, elige un elemento para saber su talla ->  "+str(diccionario_tallas))

#elemento elegido
elemento = (input("Nombre -> "))

validar = diccionario_tallas.get(elemento,'null') #Si no lo encuentra, manda el error 'ValueError'

if(validar =='null'):
    #No se encuentra 
    print("No existe dicho key!")
    
else: #Si se encuentra, mostrarlo
    print("La estatura de "+elemento+" es-> "+str(diccionario_tallas[elemento]))
