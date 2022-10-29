"""
Ejercicio 5
Dado el diccionario que almacena la talla de algunas personas 
{'Marcelo': 1.80, 'José':1.50, 'Oscar':1.70, 'Jorge': 1.40}, escriba un programa que dado un 
nombre ingresado 
por el usuario imprime la talla.

Ejemplo:

Ingrese un nombre: Marcelo

Salida: 1.80
"""
diccionario={'Marcelo': 1.80, 'José':1.50, 'Oscar':1.70, 'Jorge': 1.40}
print("Hola. esta es el diccionario -> "+str(diccionario))

salir = False

while(not salir):
    
    nombre = (input("Ingresa nombre de la persona!: "))
    #si existe o no, el numero ingresado
    try:

        #nombre=int(nombre) #si no es un numero, se manda la excepcion
        posicion=diccionario.get(nombre,'null') #si no se encuentra el elemento buscado, se manda la excepcion
        if posicion=='null':
            print("No se encontro la clave")
        else:

            print("La talla de ",nombre," es: -> ",diccionario[nombre])
            salir=True

    except ValueError:
        print("No se encontro el numero en la tupla. mira bien!")


