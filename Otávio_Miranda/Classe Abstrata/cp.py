from conta import Conta

class ContaPoupanca(Conta):
    def sacar(self, valor):
        print(f'SAQUE: {valor}')
        self.saldo -= valor
        self.mostrar_saldo()
        