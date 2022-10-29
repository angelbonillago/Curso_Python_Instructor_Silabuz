"""
Ejercicio 6
Dado el diccionario que almacena la talla de algunas personas {'Marcelo': 1.80, 'José':1.50, 'Oscar':1.70, 'Jorge': 1.40}, escriba un programa que dada una talla por el usuario imprima el nombre.

Ejemplo:
Ingrese una talla: 1.80
Salida: Marcelo

"""

diccionario_tallas= {'Marcelo': 1.80, 'José':1.50, 'Oscar':1.70, 'Jorge': 1.40}
print("De este diccionario, elige una talla ->  "+str(diccionario_tallas))

#elemento elegido


list_of_keys = list(diccionario_tallas.keys())
list_of_values = list(diccionario_tallas.values())

elemento = float(input("Talla -> "))

position = list_of_values.index(elemento)

print(list_of_keys[position])