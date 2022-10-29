"""
Ejercicio 7
Escribir un programa que reciba por teclado dos cadenas ingresadas por el usuario, luego el programa d
eberá crear una nueva cadena formada por las dos cadenas dadas, estas deben estar separadas por un espacio y 
sin vocales.

Ejemplo: si las cadenas son "cincuenta" y "sesenta" entonces la nueva cadena deverá ser "cncnt ssnt".

"""
vocales = ["a", "e", "i", "o", "u"]

try:
    cad1 = input("Ingrese la primera cadena: ")
    cad2 = input("Ingrese la segunda cadena: ")

    #Concatenando candenas
    candeaGeneral = cad1+" "+cad2
    cadenaSinVocales="";

    for i in range(len(candeaGeneral)):
        if candeaGeneral[i] not in vocales:
            cadenaSinVocales += candeaGeneral[i] # concatena
        i +=1

    print('Nueva cadena sin vocales -> ',cadenaSinVocales)
except ValueError:
    print("Numero no enteros")

