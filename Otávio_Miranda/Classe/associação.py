class Escritor:
    def __init__ (self, nome):
        self.__nome = nome
        self.ferramenta = None
    
    # Por conter '__' antes do atributo, é necessário a criação de um GETTER (@property)
    # para que consigamos acessar o atributo nome fora da classe, caso contrário dará ERRO!
    # APENAS PARA PRÁTICA
    
    @property 
    def nome(self):
        return self.__nome 
    
class Caneta:
    def __init__(self, marca):
        self.marca = marca
    
    def escrever(self):
        print('Caneta está escrevendo.')
        
class Maquina:
    def escrever(self):
        print('Maquina está escrevendo.')

    
escritor = Escritor('Gustavo')
caneta = Caneta('BIC')
maquina = Maquina()


# neste caso foi Associado maquina como a ferramenta do escritor 
escritor.ferramenta = caneta
escritor.ferramenta.escrever()



    