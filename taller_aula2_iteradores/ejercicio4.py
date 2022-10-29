"""
Pregunta 4
Escriba un generador que permita contar las letras de las palabras de una lista.

Ejemplos:

Para "humanidad": {'h': 1, 'u': 1, 'm': 1, 'a': 2, 'n': 1, 'i': 1, 'd': 2}
Para "humano": {'h': 1, 'u': 1, 'm': 1, 'a': 1, 'n': 1, 'o': 1}

{clave -> valor}

"""

def generadorContarLetras(palabra):
    diccionario={}
    for indice in list(palabra):
        cantidad=palabra.count(indice) 
        diccionario[indice]=cantidad
        yield diccionario # yield -> variable -> lo que quiero que no tome espacio en memoria 

varibale_yield= (generadorContarLetras("humanidad"))

while True:
    try:
        print(next(varibale_yield))
        print("--")
    except StopIteration:
        print("No hay mas elementos!")
        break #salgo del while


        

