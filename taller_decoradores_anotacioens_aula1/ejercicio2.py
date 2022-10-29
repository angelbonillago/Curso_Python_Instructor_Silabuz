"""
Pregunta 2
Escriba un programa que dada una entrada numérica por el usuario, ingrese a una función que duplique el 
valor y sea retornado en forma de string o cadena. Utilice tipos tanto para las variables como para las 
funciones

#anotaciones

"""
#Anotaciones

#tipos de datos 
#Colecciones
#Funciones 
#parametros


def duplicarNumero(numero:int)->str:
    return str(numero*2)
    


numero_pedido=int(input("Ingresa numero : "))

print((duplicarNumero((numero_pedido))))


