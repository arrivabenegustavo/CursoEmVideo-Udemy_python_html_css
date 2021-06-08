from abc import ABC, abstractmethod

class Conta(ABC):
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
            raise ValueError('Saldo deve ser numérico')
            return
        
        self._saldo = valor
        
    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Depósito precisa ser numérico')
            return
        print(f'DEPÓSITO: {valor}')
        self.saldo += valor
        self.mostrar_saldo()
        
    @abstractmethod    
    def sacar(self):
        pass
    
    
    def mostrar_saldo(self):
        print(f'Agência:{self.agencia}', end=' ')
        print(f'Conta:{self.conta}', end=' ')
        print(f'Saldo:{self.saldo}')    