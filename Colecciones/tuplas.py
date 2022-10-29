numeros = 1, 2, 3, 4, 5 #La forma de crear una tupla sin paréntesis es conocida como tuple packing (algo así como empaquetado de tuplas).
tup = 1, ['a', 'e', 'i', 'o', 'u'], 8.9, 'hola'
unico_elemento = ('a',) #Se creo una tuple de 1 solo elemento, por ello la coma','

#print(type(numeros))
#print(tup)

#TUPLE UNPACKING
bebidas = 'agua', 'café', 'batido'
a, b, c = bebidas
#print(b)

#Modificar una tupla en Python
tupla = (1, ['a', 'b'], 'hola', 8.2)
tupla[1].append('c')  # tupla[1] hace referencia a la lista
tupla.add('nuevo')
print(tupla)