"""
Ejercicio 4
Dada una tupla de números (1,3,5,2,7,5,5,8,4,8,4,8,4), escriba un programa que dado un elemento por el usuario, 
imprima el número de veces que se encuentra en la tupla.

Ejemplo:
Ingrese el elemento a contar: 4
Salida: 3

"""
tupla_numeros = (1,3,5,2,7,5,5,8,4,8,4,8,4)

print("De esta tupla, elige un elemento para contarlo ->  "+str(tupla_numeros))

#elemento elegido
elemento = (input("elemento -> "))

try:
    elemento = int(elemento) #Si no lo encuentra, manda el error 'ValueError'

    posicion_elemento = tupla_numeros.index(elemento) #Si no lo encuentra, manda el error 'ValueError'

    #print(posicion_elemento)
    #print("elemento valido!")

    #procede a contarlo
    print("El numero "+str(elemento)+" se encuentra "+str(tupla_numeros.count(elemento))+" veces")

except ValueError:
    print("El elemento no fue encontrado en la tupla!!!")