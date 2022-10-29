"""
Pregunta 1
Dada la lista de notas [15,20,18] y la lista de alumnos ["Marcelo", "José", "Juan"] 
Imprimirlos de la siguiente forma:

Marcelo : 15

José : 20

Juan : 18
"""
def usarZip(lista1,lista2):
  for i in zip(lista1,lista2): 
    print(i[1]," -> ",i[0],"\n") 

def recorrerNombres(lista1,lista2):
  contador =1 
  for i in zip(lista1,lista2): 
    
    nombre = i[1] #-> José
    print("Nombre -> ",contador)
    contador+=1 #
    cadena=""
    for caracter in nombre: #sirve para recorrer letra a letra, el nombre( M,a,r,c,....)
      cadena=cadena+" "+caracter #acumulando letra a letra
    print(cadena) 

def letras_repetidas():
  pass

lista1=[15,20,18,5,0,7,9,3]
lista2=["Marcelo", "José", "Juan"] 

usarZip(lista1,lista2)
recorrerNombres(lista1,lista2)

