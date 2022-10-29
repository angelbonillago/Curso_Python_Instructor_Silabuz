#zip() -> JUNTAR COLECCIONES PARA QUE SEAN ITERABLES

#"JUNTAR" VEA LISTAS DE IGUAL TAMAÑO
#LISTAS != TAMAÑO, ZIP() NO TOMARA EN CUENTA LOS ELEMENTOS SOBRANTES 

lista1=[1,4,0,7,2]
lista2=["Pedro","Marie","Maria","Luis","Orlando"]

lista_ = [i for i in zip(lista1,lista2)]



print(lista_)

mayor = 0 
for i in zip(lista1,lista2):
    #print(i[0]) #[0] -> los numeros
    if(i[0]>mayor):
        mayor=i[0]
    
#print("el mayor de la lista1 fue ",mayor)

#tuplas -> indexacion 
tupla =(5,9,2,7,11)
variable = tupla[0]
#print(variable)




