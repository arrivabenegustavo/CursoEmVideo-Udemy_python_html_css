class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__
        
    def comprar(self):
        print('Método dentro de Pessoa')      
        

class Aluno(Pessoa): # Herdou Pessoa(Classe Principal)
    def estudar(self):
        print(f'{self.nomeclasse} está estudando')         
 
   
class Cliente(Pessoa): # Herdou Pessoa(Classe Principal)
    def comprar(self):
        print('Método dentro de Cliente')


# E possível HERDAR uma classe que ja tenha herdado outra classe, além disso...
# E possível tbm sobreescrever um método que foi criado em um das classes herdadas
# Ele executa apenas o método que está dentro da classe 
# neste caso sobreescreve o método dentro de Cliente   
class ClienteVip(Cliente): # Herdou Cliente(consequentemente foram herdadas duas classes)
    def comprar(self):
        # Mas caso queira executar o outro método que foi sobreescrito, tbm é possível
        #super().comprar() # -> Desta forma ele executará a primeira que achar, caso tenha outra função
        # COMPRAR dentro de Pessoa, ele executará apenas da cLIENTE
        # Ou pode indicar direto onde deve buscar 
        print('Método dentro de cliente Vip')
        Cliente.comprar(self) # neste caso é necessário a instancia SELF
        Pessoa.comprar(self)  # neste caso é necessário a instancia SELF
        

vip1 = ClienteVip('Gustavo', 31)
vip1.comprar()



