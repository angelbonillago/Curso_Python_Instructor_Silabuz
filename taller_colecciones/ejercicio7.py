"""
Ejercicio 7
Guarde los datos de una persona (nombre,apellido,edad) en un diccionario, luego imprimalo en el siguiente 
formato. 

"Hola mi nombre es [nombre] [apellido], y tengo [edad] años.
"""
 
print("\t\tDATOS PERSONALES")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))


diccionario_personas={}
diccionario_personas["nombre"] = nombre
diccionario_personas["apellido"] = apellido
diccionario_personas["edad"] = edad

print("Hola mi nombre es", diccionario_personas["nombre"], diccionario_personas["apellido"] + ", y tengo", diccionario_personas["edad"], "años")