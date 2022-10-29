"""
# Ejercicio 1
Dada la matriz, `[[1,2,3],[4,5,6],[7,8,9]]`, calcule el promedio de la diagonal principal. Hint: 
Los 3 elementos de la diagonal son 1,5,9
"""

lista_matriz=[[1,2,3],
              [4,5,6],
              [7,8,9],] #Matriz cuadrada

"""
suma = lista_matriz[0][0]+lista_matriz[1][1]+lista_matriz[2][2]
promedio=suma/len(lista_matriz)
print(promedio)
"""
suma_=0.0
for i in range(len(lista_matriz)):
    suma_=suma_ + lista_matriz[i][i]

promedio_ = suma_/len(lista_matriz)
print("Promedio de la diag. Principal: -> "+str(promedio_))