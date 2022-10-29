"""
Ejercicio 7
Escribir una función imprime_lista_anidada_1 para imprimir listas anidadas. Cada sublista debe ser 
impresa en una línea diferente. Los elementos dentro de la sublista deben estar separados por una tabulación.
No use índices. Si el argumento es [[1,2,3],[4,5],[6,7,8,9]], la función debe imprimir: 1 2 3 4 5 6 7 8 9


"""

def imprime_lista_anidada_1(lista_anidada):
    #validar si todos las posiciones son listas,si no lo son,solo imprimo las listas anidadas.
    cadenaTabulacion=""
    for lista in lista_anidada:
        
        if((type(lista))== list):
            print(lista)
            #recorrer y mostrar con tabulacion
            for elemento in lista:
                cadenaTabulacion=cadenaTabulacion+str(elemento)+"  "


    print(cadenaTabulacion)

imprime_lista_anidada_1([[1,2,3],4,5,[6,7,8,9]])