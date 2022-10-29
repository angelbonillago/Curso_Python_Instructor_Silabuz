"""
1.  Contar el número de espacio en un string dado python
"""
def pedirDatos():
    cadena =input("Ingresa la cadena: ")
    contarEspacios(cadena)

def contarEspacios(cadena):
    contador=0
    for i in cadena:
        if(i==" "):
            contador +=1

    print("CADENA INGRESADA -> ",cadena)
    print("cantidad de espacios -> ",contador)

pedirDatos()