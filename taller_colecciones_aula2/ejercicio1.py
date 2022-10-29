"""

Ejercicio 1
Dada la matriz, [[1,2,3],[4,5,6],[7,8,9]], calcule el promedio de la 
diagonal 
principal. 
Hint: Los 3 elementos de la diagonal son 1,5,9

"""
matriz_lista=[[1,2,3],
              [4,5,6],
              [7,8,9],
              ] #matriz cuadrada m=n

suma=0.0
promedio=0.0

#primera forma
""" suma=matriz_lista[0][0]+matriz_lista[1][1]+matriz_lista[2][2]+matriz_lista[3][3]
promedio= suma/3
print(promedio) """

#2da forma
for i in range(len(matriz_lista)):  #0,1,2,3
    suma=suma+matriz_lista[i][i] 

promedio=suma/len(matriz_lista)

print("Promedio de la Diag. Pri : -> ",(promedio))








