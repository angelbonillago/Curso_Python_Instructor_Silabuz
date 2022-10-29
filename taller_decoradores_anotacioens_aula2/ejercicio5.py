"""
Problema 5
Cree una función decoradora deco1 que muestre el siguiente flujo, para cualquier número ingresado, por 
ejemplo para el número 30:

Hola, estoy decorando esta función.

Ingresaste el número 30

Terminé de decorar
"""

def deco1(funcion):
    def interno(a):
        print("Hola, estoy decorando esta función.")
        funcion(a)
        print("Terminé de decorar")
    return interno

@deco1
def mostrar_mensaje(numero):
    print("Ingresaste el número ",numero)

mostrar_mensaje([12,10,5,3])
