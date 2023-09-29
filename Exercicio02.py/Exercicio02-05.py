#Questão 5
class Pessoa:

  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

  def cumprimentar(self):
    print(f"Olá, {self.nome}! Você tem {self.idade} anos.")


nome = input("Qual seu nome? ")
idade = int(input("Informe sua idade: "))

pessoa = Pessoa(nome, idade)
pessoa.cumprimentar()
