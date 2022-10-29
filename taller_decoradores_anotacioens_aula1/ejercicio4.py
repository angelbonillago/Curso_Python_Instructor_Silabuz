"""
Pregunta 4
Dada la función "calc_par_impar" que retorna un booleano, dependiendo si el número ingresado es par o impar, 
cree un decorador que imprima que tipo de número a recibido la función.

"""
def decoradorCal(funcion):
    def interior(*args):
        if funcion(*args):
            print("Ingresaste un par")
        else:
            print("Ingresaste un impar")
    return interior

@decoradorCal
def calc_par_impar(numero): #me hace la operacion 
    #si un Num es par o impar
    if(numero % 2==0): #7 % 2 ==0
        return True
    else:
        return False
    
numero_obtenido =int(input("Ingresa numero : "))
calc_par_impar(numero_obtenido)

