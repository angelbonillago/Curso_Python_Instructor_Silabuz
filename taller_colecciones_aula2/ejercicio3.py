'''
Dada una lista de números enteros [15,20,50,80,40,60],
 escriba un programa que dado un dato por el usuario,
  este sea eliminado de la lista. Tome en cuenta que el usuario
   ingresará datos que se encuentran dentro de la lista
'''
lista=[15,20,50,80,40,60]
eliminar=int(input("Ingresar el numero a eliminar: "))
x=True

if lista==eliminar:
    lista.remove(eliminar)
        
else:
    print("Elija un numero a eliminar que este en la lista")
        
print(lista)
