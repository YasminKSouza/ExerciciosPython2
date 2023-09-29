#Questão 1
import math
class Circulo:
    def __init__(self, raio):
        self.raio = raio
    def area(self):
        return math.pi * (self.raio**2)
area = Circulo(6)
print(f"A área do círculo é igual a {area.area():.2f} cm.")