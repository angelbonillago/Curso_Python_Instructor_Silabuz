zip() #-> JUNTAR COLEECIONES! - LISTAS,TUPLAS,DICCIONARIOS,SET
      #-> SEAN DE IGUAL TAMAÑO

lista1=[1,4,9,6,5,4,5,6,7,8]
lista2=[0,8,6,5,4]

#union = zip(lista1,lista2)
mayor=0
for x in zip(lista1,lista2):
    #print(x[0]," -> ",x[1])
    #[0] edades
    #[1] -> medallas
    edades=x[0]
    medalla =x[1]
    if(mayor<edades):
        mayor=edades

#print("La edad mayor es -> ",mayor)


lista3=enumerate(range(10),start=1)
print(lista3)

print(next(lista3))
print(next(lista3))

print("----")

for f in lista3:
    print(f[0]," -> ",f[1])

