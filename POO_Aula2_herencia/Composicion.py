class Animal:
    def __init__(self,especie,peso):
        self.especie=especie
        self.peso = peso
        self.hueso=Hueso("Craneo","Plano")

    def comer(self):
        print("Animal comiendo")

    def informacion(self):
        txt="{0},{1},{2},{3}"
        return txt.format(self.especie,self.peso,self.hueso.nombre,self.hueso.tipo)

        """    
        def datos(self):
        print 
        """ 

class Hueso():
    def __init__(self,nombre,tipo) :
        self.nombre=nombre
        self.tipo=tipo

animal = Animal("Leon",300)
animal.comer()
print(animal.informacion())