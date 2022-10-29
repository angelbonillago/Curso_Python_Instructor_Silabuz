d = {1: 'hola', 89: 'Pythonista', 'a': 'b', 'c': 27,'dos':2}
d6 = dict() # Diccionario vacío usando el constructor
d5 = {} 

print(type(d))

#Cómo acceder a los elementos de un diccionario en Python
print(d['dos'])
#método get(clave[, valor por defecto]),para obtener un valor mediante su clave
print(d.get('uno')) #Proporciona None cuando no lo encuentra
print(d.get('uno','vacio'))#Proporciona Vacio cuando no lo encuentra

#Añadir elementos a un diccionario en Python
d['nuevo']='nuevo-valor'
print(d)

# --> NOTA: Si la clave ya existe en el diccionario, se actualiza su valor.
d['nuevo']='nuevo-valor, actualizado ? agregado??'
print(d)

#método setdefault(clave[, valor]), Este método devuelve el valor de la clave si ya existe
print(d.setdefault('tres', 'clave no encontrada'))