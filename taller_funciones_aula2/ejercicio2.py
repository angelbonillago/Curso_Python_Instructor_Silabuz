"""
Ejercicio 2
Plantear 2 formas de encontrar los números comunes entre 2 
listas sin usar set.

"""
def primeraForma():
    lista1=[1,5,9,6,3,10,21,21,21]
    lista2=[4,8,9,6,5,2,21,21,21]
    valores_comunes=[]

    for i in range(len(lista1)):
        for x in range(len(lista2)):
            existe= lista2[x] in valores_comunes
            if(lista1[i]==lista2[x] and not existe):
                valores_comunes.append(lista2[x])

    print(valores_comunes)

def segundaForma():
    print("?")

