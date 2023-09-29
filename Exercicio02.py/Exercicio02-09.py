#Questão 9
class Aluno():

  def __init__(self, nome, nota1, nota2):
    self.nome = nome
    self.nota1 = nota1
    self.nota2 = nota2

  def media(self):
    media = (self.nota1 + self.nota2) / 2
    print(f"A média de {self.nome} é {media:.2f}")


nome = input("Digite o nome do aluno: ")
n1 = float(input("Digite a 1º nota: "))
n2 = float(input("Digite a 2º nota: "))

aluno = Aluno(nome, n1, n2)
aluno.media()
