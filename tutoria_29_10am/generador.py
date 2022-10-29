"""
contar las caracteres repetidos de una palabra.

humano
{'h':1,'u:1.......}

"""

def contarPalabras(palabra): #perro
    diccionario={}
    for caracter in palabra:
        cantidad=palabra.count(caracter)
        #diccionario={caracter:cantidad}
        diccionario[caracter]=cantidad
        yield diccionario


contenido_yield=(contarPalabras("humanidades"))
#print(contenido_yield)

print(next(contenido_yield))
print(next(contenido_yield))
print(next(contenido_yield))

print('------------')



while True:
    try:
        print(next(contenido_yield))
    except StopIteration:
        print("No hay mas elementos")
        break
