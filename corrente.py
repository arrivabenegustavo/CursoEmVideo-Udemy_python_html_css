from contas import Contas

class ContaCorrente(Contas):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self._limite = limite
        
    @property
    def limite(self):
        return self._limite
    
    def saque(self, valor):
        print(f'Saque: {valor:.2f}')
        if valor > (self.saldo + self.limite):
            print('Saldo insuficiente')
            print('-'*40)
            return
        self.saldo -= valor
        self.ver_saldo()
        print('-'*40)