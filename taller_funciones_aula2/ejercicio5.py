"""
Ejercicio 5

Escribir una función extrae_columna_n que reciba como parámetro una lista M y un valor n. 
La función debe extraer los valores "de la columna" n específica a la lista anidada dada. 
La función debe verificar que n esté en el rango permitido. Caso contrario, la función debe retornar una 
lista vacía.


Ejemplo:
M = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
n = 0

Para extrae_column_n(M, n) la función retornará [1, 2, 1]

"""

def extrae_columna_n(M,n):
    #M -> es la lista 
    #n -> es la posicion a obtener
    try:
        #existe=M[n]
        print(M[n])

    except IndexError:
        print([])


extrae_columna_n([[1, 2, 3], [2, 4, 5], [1, 1, 1]],8)