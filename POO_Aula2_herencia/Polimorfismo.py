#Polimorfismo ->Poli : Muchos,Morfos :formas


class Estudiante():
    def describir(self):
        print("Soy estudiante")


class Docente():
    def describir(self):
        print("Soy Docente")

class Trabajador():
    def describir(self):
        print("Soy Trabajador")

def obtener_clase(persona):
    persona.describir()

obj_persona = Trabajador()
obtener_clase(obj_persona)