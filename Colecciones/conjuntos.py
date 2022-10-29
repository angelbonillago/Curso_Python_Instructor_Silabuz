c = {1, 3, 2, 9, 3, 1}
#print(type(c))

a = set('Holagrupo')
#print(a)

#creando un conjunto desde una tupla,lista,dicc
tup = 1, 8.9, 'hola',7
lista_1 = [3, 7, 9]


conjunto1 = set(lista_1)
print(type(conjunto1))

conjunto2 = set(tup)
print(type(conjunto2))

#NOTA: {} NO crea un conjunto vacío, sino un diccionario vacío. Usa set() si quieres crear un conjunto sin elementos.

#ACCEDER A LOS ELEMENTOS DE UN CONJUNTO
for e in conjunto2:
    print(e)


#Añadir elementos a un conjunto (set) en Python
conjunto2.add(7)
print(conjunto2)

#OPERACIONES CON CONJUNTOS
print("UNION")
print(conjunto1 | conjunto2)
print(conjunto1.union(conjunto2))

print("INTERSECCION")
print(conjunto1 & conjunto2)
print(conjunto1.intersection(conjunto2))

print("INTERSECCION")
print(conjunto1 - conjunto2)
print(conjunto1.difference(conjunto2))

#discard(elemento) y remove(elemento) eliminan elemento del conjunto. 
#La única diferencia es que si elemento no existe, discard() no hace nada mientras que remove() lanza la excepción KeyError.


#CONSIDERACIONES CON SET

#s1 = {2, 4, [4, 8]}
#s2 = {"Paris", "Madrid", {"city": "London", "country": "England"}}
#s3 = {2, 4, {4, 8}}

#print(s1)
#print(s2)
#print(s3)


#FROZEN SET

"""
En realidad, en Python existen dos clases para representar conjuntos: set y frozenset. 
La principal diferencia es que set es mutable, por lo que después de ser creado, se pueden añadir y/o eliminar
elementos del conjunto, como veremos en secciones posteriores. Por su parte, frozenset es inmutable y 
su contenido no puede ser modificado una vez que ha sido inicializado.

"""

fr_s1 = frozenset(["Paris", "Madrid"])
fr_s2 = frozenset(["Roma", "Milan"])
print({fr_s1, fr_s2})
print(type(fr_s1))

fr_s1.add('a') #AttributeError: 'frozenset' object has no attribute 'add'

