from math import *
import os
import shutil
from datetime import *

#print(sin(90))
#print(cos(0))
""" 

print("ruta principal -> ",os.getcwd())
print("ruta principal -> ",os.system('rmdir prueba_modulo'))

"""

#shutil.copyfile("TEORIA_COLECCIONES.txt","copiado.txt")
#shutil.move('TEORIA_COLECCIONES.txt','/prueba/dos')


tiempo = date.today()
#print(tiempo)

#datetime.date(2022,26,10)

birth = date(1995,10,26)
age = tiempo-birth
print(age.days)





