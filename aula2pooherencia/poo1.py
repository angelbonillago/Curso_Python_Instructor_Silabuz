class Vechiculo: #clase padre
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
    def informacionVeviculo(self): #ESTA ES LA Fx QUE SE HEREDA A SUS CLASES HIJAS!
        txt="{0},{1}"
        return txt.format(self.marca,self.modelo)
    def datos(self):
        print(self.informacionVeviculo())

class Carro(Vechiculo):
    
    def __init__(self, marca, modelo,estado):
        super().__init__(marca, modelo) #me trae la info de mi clase Padre(Vehiculo!)
        self.estado=estado#propiedad unica de la clase hija Carro

    #NO TENGO NINGUN METODO CREADO!!!
    def datos(self):
        super().datos() #info del padre + info. del la clase hija
        print("Estado del carro {0}".format(self.estado))


class Camion(Vechiculo):
    def __init__(self, marca, modelo,longitud):
        super().__init__(marca, modelo)
        self.longitud=longitud

    def datos(self):
        super().datos()
        print("Longitud del camion {0}".format(self.longitud))

class Tico(Vechiculo):
    def __init__(self, marca, modelo,color):
        super().__init__(marca, modelo)
        self.color=color

    def datos(self):
        super().datos()
        print("Color del Tico {0}".format(self.color))


objeto_carro1=Carro("TOYOTA","DEPORTIVO","OK") 
objeto_carro1.datos()

print("------- ")
objeto_tico=Tico("NISSA","PEQUEÑO","AMARILLO")
objeto_tico.datos()

print("------- ")
objeto_camion=Camion("CAMOION POWER","NUEVO",5)
objeto_camion.datos()
