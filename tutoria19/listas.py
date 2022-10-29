lista_mentoria =[4,5,6,9,'PRUEBA',10.5,False,True,['a','e','i','o','u'],(4,9,8),{'id':15},{1,8,9,6,6},'PRUEBA','PRUEBA']

print(lista_mentoria)
print("Ahora si, elimina alguno ")
indice =  (input("Ingresa elemento a eliminar: ->  ")) #6


if(indice==""):
    print("No ingreses algo vacio")
    exit()
elif(int(indice)>0 or int(indice) <0):
     indice=int(indice)


posicion= lista_mentoria.index(indice)
lista_mentoria.pop(posicion)


print("resultado de la eliminacion")
print(lista_mentoria)







#print(lista_mentoria.count(10.5))

#print(type(lista_mentoria))
"""
lista_nombre=[]
limite = 0
salir=False

limite= int(input("Ingresa de numero de nombres a guardar: ->  "))  

while(not salir):
    nombre= input("nombre -> ")
    lista_nombre.append(nombre)
    limite =limite-1  # limite -=1

    if(limite==0):
        salir=True

print('LOS NOMBRES QUE SE INGRESO')
print(lista_nombre)

print('ELIMINAR ULTIMO NOMBRE')
lista_nombre.pop()  # -> ELIMNINAR EL ULTIMO ELEMENTO INGRESADO

print(lista_nombre)


"""









