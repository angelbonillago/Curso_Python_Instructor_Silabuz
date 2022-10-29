diccionario ={1:'prueba',2:'valor'}

def dividir(dividendo,divisor):

    try:
    #diccionario[4] #accediendo a una clave que no existe! 
        #error de tipo Key Error 
        resultado =dividendo/divisor
        print(resultado)  
    except ZeroDivisionError:
        print("No dividas entre 0")

dividir(10,5) #/