#Questão 10
class Funcionario():

  def __init__(self, nome, salario, cargo):
    self.nome = nome
    self.salario = salario
    self.cargo = cargo

  def aumentar_salario(self, aumento):
    novo_salario = self.salario + (self.salario * (aumento / 100))
    print("=" * 50)
    print(
        f"Funcionário: {self.nome}\nSalário Antigo: R$ {self.salario:.2f}\nSalário Atual: R$ {novo_salario:.2f}"
    )
    print("=" * 50)


nome = input("Informe o nome do funcionário: ")
salario = float(input("Digite o salário de " + nome + ": R$ "))
cargo = input("Qual o cargo atual? ")
aumento = float(input("Qual o % de aumento aplicado para " + nome + "? "))

funcionario = Funcionario(nome, salario, cargo)
funcionario.aumentar_salario(aumento)
