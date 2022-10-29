"""
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y 
el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que
dura la inversión.

"""

def armarDiccionario():
    global diccionario
    diccionario={}

    diccionario['cantidad_invertir']=cantidad_invertir
    diccionario['interes_anual']=interes_anual
    diccionario['numero_anos']=numero_anos
    return diccionario

def pedirDataUsuario():
    #pedimos info.
    global cantidad_invertir
    global interes_anual
    global numero_anos
    

    cantidad_invertir = float(input("Ingresa cantidad a invertir: -> "))
    interes_anual = float(input("Ingresa interés anual : -> "))
    numero_anos = int(input("Ingresa numeros de años : -> "))

    #mandar la info. a la funcion armarDicc
    armarDiccionario()

def obtenerInteres_ano():
    return ((interes_anual/100)*cantidad_invertir) * numero_anos


#Instrucciones o el llamado a las funciones
pedirDataUsuario()
armarDiccionario()
print("El interes por ",numero_anos," años es -> ",obtenerInteres_ano())








