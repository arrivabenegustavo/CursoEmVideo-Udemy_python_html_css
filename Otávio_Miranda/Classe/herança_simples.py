'''
A herança faz com que outras classes herdem outras classes
fazendo com que a classe herdada seja considerada uma SUPER CLASSE
e as classes que herdaram um SUBCLASSE
isso é necessário quando existe mais de uma classe com as mesma informações
o que as diferencia são apenas especificações como no exemplo abaixo
'''
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__
        
class Cliente(Pessoa):
    def comprar(self): # esse método pertence apenas a está classe
        print(f'{self.nomeclasse} está comprando')


class Aluno(Pessoa):
    pass

c1 = Cliente('Gustavo', 31)
c1.comprar()