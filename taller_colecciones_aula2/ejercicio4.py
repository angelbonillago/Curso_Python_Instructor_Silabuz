"""
Ejercicio 4
Dada una tupla de números (1,3,5,2,7,5,5,8,4,8,4,8,4), escriba un programa que dado un 
elemento por el usuario, 
imprima el número de veces que se encuentra en la tupla.

Ejemplo:
Ingrese el elemento a contar: 4
Salida: 3

"""
tupla_numero = (1,3,5,2,7,5,5,8,4,8,4,8,4)
print("Hola. esta es la tupla -> "+str(tupla_numero))
salir = False

while(not salir):
    
    numero = (input("Ingresa numero!: "))
    #si existe o no, el numero ingresado
    try:

        numero=int(numero) #si no es un numero, se manda la excepcion
        posicion=tupla_numero.index(numero) #si no se encuentra el elemento buscado, se manda la excepcion
        if posicion>=0:
             cantidad= tupla_numero.count(numero)
             print("La cantidad del numero ",numero," en la tupla es: -> ",cantidad)
             salir=True

    except ValueError:
        print("No se encontro el numero en la tupla. mira bien!")






