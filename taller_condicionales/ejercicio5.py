"""
Ejercicio 5
Escriba un programa que reciba un número n ingresado por teclado por el usuario e imprima la tabla de 
multiplicar de n desde 1 hasta 100.

"""
i = 1

try: 
    n = int(input("Ingrese el número a mostrar: "))
    while i <= 100:
        print(n,"x",i,"=",n*i)
        i+=1
        

except ValueError:
    print("Numero no enteros")


