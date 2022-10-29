"""
Ejercicio 6
Escribir un programa que imprima la serie de Fibonacci entre 0 y 100. La serie de Fibonacci; es una secuencia 
ordenada de números donde cada número siguiente se encuentra sumando los dos números anteriores.

ejemplo :  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
"""
actual = 0
sig = 1
temp = 0
serie=""

while actual <= 100:

    if(actual==0):
        serie = serie + str(actual)
    else:        
        serie = serie+" ,"+ str(actual)

    temp = actual
    actual = sig
    sig += temp

print("SERIE -> ",serie)