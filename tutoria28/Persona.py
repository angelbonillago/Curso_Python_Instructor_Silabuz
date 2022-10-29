class Persona():

    def __init__(self, dni,nombre,apellido):
        self.dni=dni
        self.nombre=nombre
        self.apellido=apellido

    def __str__(self):
        return " %s: %s, %s" % (str(self.dni), self.apellido, self.nombre)

class Trabajador(Persona):
    #herencia
    def __init__(self, dni,nombre,apellido,uniforme):
        #Persona.__init__(self,dni,nombre,apellido)
        super().__init__(dni,nombre,apellido)
        self.uniforme=uniforme
    #NO EH CREADO NINGUN METODO

trabjador1= Trabajador('7265934',"Pedro","Marquez","Uniforme ADIDAS") #eh creado informacion de un trabajador1
trabjador2= Trabajador('7465934',"Piter","Maldonado","Uniforme PUMA") #eh creado informacion de un trabajador2

print(trabjador1)
print("---------")
print(trabjador2)