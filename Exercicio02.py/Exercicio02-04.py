#Questão 4
class ContaBancaria:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def status(self):
        print(f"Saldo: R$ {self.saldo}")

    def depositar(self, valor):
        self.saldo += valor
        print(f"Deposito de R$ {valor} realizado com sucesso.\nNovo saldo: R${self.saldo}")


    def sacar(self, valor):

        if self.saldo < valor:
            print("Saldo insufuciente!")

        else:
            self.saldo -= valor
            print(f"Saque de R$ {valor} realizado com sucesso.\nNovo saldo: R${self.saldo}")

print("Bem Vindo ao Banco XEN")
print("=" * 30)
nome = str(input("Qual seu usuário? "))
print("=" * 30)
ver = ContaBancaria(nome, 5000)


while True:

    print("[1] Ver saldo\n[2] Depositar\n[3] Sacar\n[0] Sair")
    opcao = int(input("Digite uma opção: "))
    print("=" * 30)
    if (opcao == 1):
        ver.status()
        print("="*30)
    elif(opcao == 2):
        valor = int(input("Quanto você deseja depositar? "))
        ver.depositar(valor)
        print("=" * 30)
    elif (opcao == 3):
        valor = int(input("Quanto você deseja sacar? "))
        ver.sacar(valor)
        print("=" * 30)
    elif (opcao == 0):
        print("Fim da execução")
        break
    else:
        print("Opção inválida!")
        print("=" * 30)