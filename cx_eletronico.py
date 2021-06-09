from contas import Contas
from poupanca import ContaPoupanca
from corrente import ContaCorrente
from perfumaria import cabecalho


cabecalho('CONTA POUPANÇA')
cp = ContaPoupanca(167, 746510, 0)    
cp.deposito(300) 
cp.saque(150)


cabecalho('CONTA CORRENTE')
cc = ContaCorrente(1989, 41089, 0)
cc.deposito(650)
cc.saque(200)
cc.saque(500)
cc.saque(200)