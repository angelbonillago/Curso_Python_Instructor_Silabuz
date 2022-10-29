"""
Pregunta 4
Escriba un generador que permita contar las letras de las palabras de una lista.

Ejemplos:
Para "humanidad": {'h': 1, 'u': 1, 'm': 1, 'a': 2, 'n': 1, 'i': 1, 'd': 2}
Para "humano": {'h': 1, 'u': 1, 'm': 1, 'a': 1, 'n': 1, 'o': 1}

"""

def contarLetras(palabra):
    diccionario={}
    for caracter in palabra:
        #print(i)
        cantidad=palabra.count(caracter)
        #diccionario={caracter:cantidad}
        diccionario[caracter]=cantidad
        yield diccionario
    
diccionario_obtenido=(contarLetras("humano"))
print(diccionario_obtenido)

for i in diccionario_obtenido:
    print(i)