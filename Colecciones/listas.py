lista = []
#print(type(lista))

elementos = [3, 'a', 8, 7.2, 'hola',True]
#print(elementos)

lista_compleja = [1, ['a', 'e', 'i', 'o', 'u'], 8.9, 'hola']
#print(lista_compleja[1])


#concatenar listas
lista1 = [10, 20, 30, 40]
lista2 = [30, 20]
lista = lista1 + lista2 + lista1
#print(lista)


#No se puede concatenar listas con otro tipo de dato, solo con puras listas
vocales = ["E", "I", "O"]
#vocales = vocales + "A"
#print(vocales)

#listan = list({9,3,5})
listan = list('935')
#print(dir(listan)) #el metodo dir() devuelve la lista de atributos válidos del objeto pasado
#print(listan.count('9')) #el metodo count() devuelve la cantidad de caracteres repetidos en una lista


#El método list.extend() es equivalente a list[len(list):] = iterable (agrega los elementos del iterable después del último elemento de la lista)
vocales.extend(listan)
vocales.append('nuevo')
vocales.index('nuevo')
vocales.insert(2,'posicion2')
#print(vocales.index('nuevo'))

vocales.pop() #elimina el ultimo elemento de la lista
vocales.clear() #elimina todos los elementos de la lista

#print(sum(lista1))
#print(min(lista1))
#print(max(lista1))
#print(vocales)


#CONCATENANDO Y REPITIENDO LISTAS
lista_1 = [3, 7, 9]
lista_2 = [2, 0, -3]
#lista_1=2*lista_1
#print(2 * lista_1 + 3 * lista_2)

#COMPARANDO LISTAS
lista_1 = [3, 7]
lista_2 = [2, 5]
lista_3 = [3, 71]

print(lista_1 == lista_3)
print(71 in lista_1)









