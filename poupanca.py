from contas import Contas

class ContaPoupanca(Contas):
    def saque(self, valor):
        print(f'Saque: {valor:.2f}')
        if valor > self.saldo:
            print('Saldo insuficiente')
            print('-'*40)
            return
        self.saldo -= valor
        self.ver_saldo()
        print('-'*40)
        
    