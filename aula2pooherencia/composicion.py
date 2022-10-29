class Animal:
    def __init__(self,especie,peso,nombre):
        self.especie=especie
        self.peso=peso
        self.nombre=nombre
        self.hueso=Hueso("Craneo","Plano",30)

    def comer(self):
        print("El animal come")

    def corre(self):
        print("El animal corre")

    def informacion(self):
        txt="{0},{1},{2},{3},{4},{5}"
        return txt.format(self.especie,self.nombre,self.peso,self.hueso.nombre,self.hueso.tipo,self.hueso.longitud)

    def datos(self):
        print(self.informacion())
    
class Hueso():
    def __init__(self,nombre,tipo,longitud):
        self.nombre=nombre
        self.tipo=tipo 
        self.longitud=longitud     

obj_leon=Animal(especie="Felino",nombre="Leon",peso=300)
obj_leon.datos()

