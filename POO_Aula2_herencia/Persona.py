class Persona():
    #caracteristicas de 1 persona!
    def __init__(self,dni,apellido,nombre,sexo):
        self.dni=dni
        self.apellido=apellido
        self.nombre=nombre
        self.sexo=sexo

    def dameDatosPersona(self):
        txt="{0},{1},{2},{3}"
        return txt.format(self.dni,self.apellido,self.nombre,self.sexo)
    
    def datos(self):
        print(self.dameDatosPersona())
#heredar

class Estudiante(Persona):
    def __init__(self, dni, apellido, nombre, sexo,carrera):
        super().__init__(dni, apellido, nombre, sexo)
        self.carrera=carrera

    #AQUI NO TENGO NINGUN METODO CREADO!!!!
    def datos(self):
        super().datos()
        print("Profesion: {0}".format(self.carrera))
  

class Docente(Persona):
    def __init__(self, dni, apellido, nombre, sexo):
        super().__init__(dni, apellido, nombre, sexo)



objeto_estudiante1=Estudiante(75832364,'Flores','Marie','F','Analista')
#objeto_estudiante=Estudiante(75866340,'Daniel','Escriba','M','Programador')

#objeto_docente1= Docente(75832366,'Bonilla','Angel','M')


objeto_estudiante1.datos()

