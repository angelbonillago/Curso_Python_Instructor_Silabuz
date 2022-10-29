"""
Ejercicio 8
Dada una lista l, escribir un programa que cree una nueva lista sin los elementos duplicados. 
Utilice operador in o not in.

Si la lista es [500,100,200,300,200,100,600,400,800,400,500,900] el programa debe crear una nueva lista 
que contenga [500, 100, 200, 300, 600, 400, 800, 900]
"""

lista_original = [500,100,200,300,200,100,600,400,800,400,500,900]
lista_nueva = []

i = 0
for i in range(len(lista_original)): #0 hasta el 9
    cantidad= lista_original.count(lista_original[i])
    #print(cantidad)
    existe = lista_original[i] in lista_nueva
    #print(existe)

    if(cantidad>=1 and (not existe) ): 
        #agregamos a la lista nueva, solo uno
        lista_nueva.append(lista_original[i])


print("Lista original ",lista_original)
print("Lista Nueva ",lista_nueva) 