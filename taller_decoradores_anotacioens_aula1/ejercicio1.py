"""
Prengunta 1
Implementar la función get_avg que calcule el promedio de una lista de números:

def get_avg(lista):
  lista = [10, 40, 20, 45, 25, 35, 15]
  pass
La función get_avg retorna un float.

Asimismo implementar un decorador que permita imprimir los siguientes mensajes:

Inicio del cálculo del promedio de la lista de números.
El cálculo ha finalizado.
Entre ambos mensajes debe realizarse el cálculo del promedio de números.

"""
def decorador(funcion):
    def interior(lista):
        #operaciones y llamado 
        print("Inicio del cálculo del promedio de la lista de números.")
        funcion(lista) #print("El promedio es: ",promedio)
        print("El cálculo ha finalizado.")

    return interior

@decorador
def get_avg(lista):
  #lista = [10, 40, 20, 45, 25, 35, 15] #suma de todos y luego, divirlo entre la cant. de elementos.
  promedio = sum(lista) / len(lista)
  print("El promedio es: ",promedio)
  
lista = [10, 40, 20, 45, 25, 35, 15]
get_avg(lista)