"""
Pregunta 4
Escriba un generador que permita contar las letras de las palabras de una lista.

Ejemplos:

Para "humanidad": {'h': 1, 'u': 1, 'm': 1, 'a': 2, 'n': 1, 'i': 1, 'd': 2}
Para "humano": {'h': 1, 'u': 1, 'm': 1, 'a': 1, 'n': 1, 'o': 1}

"""

def funcionContarLetras(palabra):
    diccionario={}
    for caracter in palabra:
        cantidad=palabra.count(caracter)
        diccionario[caracter]=cantidad
        yield diccionario
    
variable_yield=(funcionContarLetras("humanidad"))

#for a in variable_yield:
 #   print(a)[]



while True:
    try:
        print(next(variable_yield))
        print('----')
    except:
        print("No hay mas elementos en el dicc")
        break





    