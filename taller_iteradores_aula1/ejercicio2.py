#zip -> juntar listar y volverlas iterables/ al ser iterables, yo las puedo recorrer

"""

2. Dada la lista de notas [15,20,18] y la lista de alumnos ["Marcelo", "José", "Juan"] 
Imprimirlos de la siguiente forma:

Marcelo : 15

José : 20

Juan : 18


"""
def fibonacci ():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


print ((fibonacci ()))

