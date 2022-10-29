
def decorador1(sumar):
    def interna():
        #bloque de codigo
        print("dentro del interna()")
        sumar()
        print("saldremos del interna()")
    
    return interna   

@decorador1
def sumar():
    a=10
    b=5
    print("suma -> ",(a+b))
    

if __name__ == '__main__':
    sumar() #se llama a la funcion sumar()
