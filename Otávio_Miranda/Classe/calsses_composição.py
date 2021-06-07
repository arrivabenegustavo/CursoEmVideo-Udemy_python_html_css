class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []
    
    # Nessa função foi feita a Composição, onde usamos a Classe Endereço
    # dentro da Classe Cliente, fazendo com que Endereço perteça a Cliente    
    def inserir_end(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))
        
    def lista_end(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)    
        
class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado
        

cliente1 = Cliente('Gustavo', 31)
cliente1.inserir_end('Osasco', 'São Paulo')
cliente1.inserir_end('Carapicuiba', 'São Paulo')
print(cliente1.nome)
cliente1.lista_end()
print()
cliente2 = Cliente('Thais', 25)
cliente2.inserir_end('Osasco', 'São Paulo')
print(cliente2.nome)
cliente2.lista_end()

# Por Endereco pertencer a Cliente, caso um dos cliente seja apagado o endereço será apagado junto


