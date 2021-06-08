from cp import ContaPoupanca
from cc import ContaCorrente


print('POUPANÇA')
print('-'*20)
p = ContaPoupanca(1989, 280821, 0)
p.depositar(100)

print()

print('CORRENTE')
print('-'*20)
c = ContaCorrente(167, 746510, 0)
c.depositar(450)
c.sacar(100)
c.sacar(200)