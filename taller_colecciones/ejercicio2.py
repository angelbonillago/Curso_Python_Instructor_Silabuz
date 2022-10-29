"""
ejercicio2

Dada la siguiente lista ["Hola", "Amigos", "Hoy", True] , escriba un 
programa que pida al usuario una palabra, dicha palabra debe ser 
agregada al final y al inicio de la lista.

"""

lista_2 = ["Hola", "Amigos", "Hoy", True]
palabra = input("Ingrese una nueva palabra: ")

if(palabra==""): #validar si el usuario ingreso una cadena vacia.
    print("No ingreses algo vacio")
    
else:
    #agregando al incio
    lista_2.insert(0, palabra)

    #agregando al final
    lista_2.append(palabra)

    #Muestro la lista 
    print(lista_2)




