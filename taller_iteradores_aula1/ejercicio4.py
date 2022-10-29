"""
Pregunta 4
Escriba un generador que permita contar las letras de las palabras de una lista.

Ejemplos:

Para "humanidad": {'h': 1, 'u': 1, 'm': 1, 'a': 2, 'n': 1, 'i': 1, 'd': 2}
Para "humano": {'h': 1, 'u': 1, 'm': 1, 'a': 1, 'n': 1, 'o': 1}

"""
#GENERADORES-> PERMITEN EXTAER VALORES DE UNA FUNCUION Y LO GUARDA DE UNO EN UNO(next()) en objetos generadores

def generadorContarLetras(palabra):
    diccionario={}
    for indice in list(palabra): 
        #cantidad=palabra.count(indice) #cuantas letras hay repetidas
        diccionario[indice] = palabra.count(indice)
        yield diccionario
    print("mensaje pruebas ",diccionario)

objetoIterable=(generadorContarLetras("humanidad"))

#print(next(objetoIterable,"null"))


""" while True:
    try:
        print(next(objetoIterable))
        print("---------")

    except StopIteration:
        print("Ya no hay mas elementos")
        break

 """

