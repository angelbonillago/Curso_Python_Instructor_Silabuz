def decorador_division(funcion_normal):
    def interno(a,b):
        print("entro")
        result = funcion_normal(a,b) #faltaria los pa.
        mostrarMensaje(result)
        print("salir")
    return interno

@decorador_division
def funcion_normal(a,b):
    division = a/b
    return division

def mostrarMensaje(result):
    print(result)

(funcion_normal(150,5))