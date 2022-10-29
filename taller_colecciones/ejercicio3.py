"""
Ejercicio 3
Dada una lista de números enteros [15,20,50,80,40,60], escriba un programa que dado un dato por el usuario, 
este sea eliminado de la lista. Tome en cuenta que el usuario ingresará datos que se encuentran dentro de la 
lista

Ejemplo:

Ingrese el dato a eliminar: 60
Salida: [15,20,50,80,40]

"""

lista = [15,20,50,80,40,60]
print("De esta lista, elige uno a eliminar ->  "+str(lista))

#elemento elegido
elemento = (input("Ingrese el dato a eliminar-> "))

#validare si el elemento ingresado, existe:
try:
    #me validara si es o no un int, en caso no lo sea, genera la excepcion
    elemento = int(elemento)

    #ingreso un numero
    posicion_elemento = lista.index(elemento)

    #print(posicion_elemento)
    print("elemento valido!")

    #procede a eliminarlo
    lista.pop(posicion_elemento)

    #muestra la lista
    print(lista) 
        
except ValueError:
    
    print("El elemento no fue encontrado en la lista!!!")








