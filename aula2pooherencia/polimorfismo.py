class Estudiante():
       
    def escribir(self):
        print("Soy estudiante")
    def sueldo(self,comisiones):
        print("El pago es : ",comisiones)


class Docente():
    def escribir(self):
        print("Soy Docente")
    
    def sueldo(self,horas,dias):
        print("El pago es : ",dias*horas)

class Trabajador():

    def escribir(self):
        print("Soy trabajador")
    
    def sueldo(self,horas,dias,bono):
        print("El pago es : ",(dias*horas)+bono)

def obtner_clase(persona):
    persona.sueldo(8,5,200)

obj_trabajador=Trabajador()
obj_docente=Docente()
obj_estudiante=Estudiante()

obtner_clase(obj_trabajador)