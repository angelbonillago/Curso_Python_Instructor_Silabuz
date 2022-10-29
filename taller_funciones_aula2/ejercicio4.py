"""
Ejercicio 

Para los números entre 10 y 500, expresar en un diccionario el número y su 
respectivo dígito más alto por el cuál es divisible. Por ejemplo para 328 es 8.

"""

def digitoMayor():
    diccionario_numeros={}
    for numero in range(10,500):
        mayor=0
        key=numero
        numero = list(str(numero))
        for x in numero:
            x=int(x)
            if(mayor < x):
                mayor=x
                diccionario_numeros[key]=mayor
        
    print(diccionario_numeros)

digitoMayor()