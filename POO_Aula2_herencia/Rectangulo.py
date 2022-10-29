class Rectangulo:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura

    def area(self):
        return self.altura*self.base

class Cuadrado(Rectangulo):
    
    def __init__(self, base, altura):
        super().__init__(base, altura)


cuadr1 = Cuadrado(5,5)
print("el area del cuadrado es -> ",cuadr1.area())