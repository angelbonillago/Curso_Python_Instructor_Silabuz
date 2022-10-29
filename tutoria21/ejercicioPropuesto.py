"""
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y 
el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que
dura la inversión.

"""

#pedir al usuario 3 cantidades
cantidad_invertir = float(input("Ingresa cantidad a invertir: -> "))
interés_anual = float(input("Ingresa interés anual : -> "))
numero_anos = int(input("Ingresa numeros de años : -> "))


#Capital obtenido
capital_obtenido=0.0
interes_obtenido_ano = 0.0
# (cantidad_invertir +(( interes_anual(cantidad_invertir))*años
interes_obtenido_ano= ((interés_anual/100)*cantidad_invertir) * numero_anos

print("En ",numero_anos," años la ganancia obtenida es : ",interes_obtenido_ano)


