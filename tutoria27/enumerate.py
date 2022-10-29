#enumerate(lista , start=2)

lista = ['Hola',True,5,13.5]
lista2=[1,5,6,9,10,7]

varib = zip(enumerate(lista,start=5),lista2)

for i in varib:
    print(i[1])

exit()

for contador,valor in enumerate(lista,start=5):
    print("Elemento ",contador," --> ",valor)
