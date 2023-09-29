#Questão 3
class Retangulo():
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    def area(self):
        return self.largura * self.altura

areaRetangulo = Retangulo(50, 15)
print(f"A área do retângulo é igual a {areaRetangulo.area()} cm.")