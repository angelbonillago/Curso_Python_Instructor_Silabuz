"""
Ejericio 4
Escribir un programa que reciba por teclado los tres lados(cm) de un triángulo ingresados por el usuario y compruebe si es un triángulo equilátero, isósceles o escaleno.

Un triángulo es equilátero si tiene los tres lados iguales.
Un triángulo es escaleno si tiene los tres lados desiguales.
Un triángulo es isósceles si tiene al menos dos lados iguales.

"""
try:
    lado_1 = float(input("Ingrese el primer lado: "))
    lado_2 = float(input("Ingrese el segundo lado: "))
    lado_3 = float(input("Ingrese el tercer lado: "))

    if lado_1 == lado_2 and lado_1 == lado_3:
        print("Triángulo equilátero")
    elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
        print("Triángulo isósceles")
    else:
        print("Triángulo escaleno")

except ValueError:
    print("tamaños no enteros")

