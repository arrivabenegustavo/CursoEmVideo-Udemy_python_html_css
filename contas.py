from abc import ABC, abstractmethod

class Contas(ABC):
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo
        
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def conta(self):
        return self._conta
    
    @property
    def saldo(self):
        return self._saldo
    
     
    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Saldo precisa ser numérico')
            return
        self._saldo = valor
    
            
    def ver_saldo(self):
        print(f'AGÊNCIA:{self.agencia}', end=' ')
        print(f'CONTA:{self.conta}',end=' ')
        print(f'SALDO:{self.saldo:.2f}')
            

    def deposito(self, valor):
        print(f'Depósito: {valor:.2f}')
        self.saldo += valor
        self.ver_saldo()
        print('-'*40)
        
        
    @abstractmethod   
    def saque(self):
        pass
        
    
    
   