# Classe Conta Corrente: Crie uma classe para implementar uma conta corrente.
# Atributos: número da conta, nome do correntista e saldo.
# Métodos são os seguintes: alterarNome, depósito e saque; No construtor,
# saldo é opcional, com valor default zero e os demais atributos são obrigatórios.

class ContaCorrente:
    def __init__(self, num, nome, saldo=0) -> None:
        self.num = num
        self.nome = nome
        self. saldo = saldo

    def alterarNome(self, novoNome):
        self.nome = novoNome

    def deposito(self, novoSaldo):
        print('Depositado com sucesso!')
        self.saldo += novoSaldo

    def saque(self, novoSaldo):
        print('Saque efetuado!')
        self.saldo -= novoSaldo

    def mostrarSaldo(self):
        print(f'Saldo: {self.saldo}')



cc = ContaCorrente(1, 'Ricardo')

cc.mostrarSaldo()
cc.deposito(25)
cc.mostrarSaldo()
cc.saque(13)
cc.mostrarSaldo()