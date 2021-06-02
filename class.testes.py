class Produto:
    
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))
        
        
    #Getter -> Obtem um valor
    @property              
    def preco(self): # A função precisa ter o mesmo nome da instancia a ser obtida
        return self._preco # Usamos um '_" antes do nome apenas para diferenciar do original 
                        # e matemos o nome para saber qual instancia estamos retornando
    #Setter
    @preco.setter # configura a instancia pedida, que neste caso é o PRECO  
    def preco(self, valor):
        if isinstance(valor, str): # Se a instancia for uma string
            valor = float(valor.replace('RS', ''))
        self._preco = valor
 
p1 = Produto('Boné', 189)
p1.desconto(10)
print(p1.nome, p1.preco) # como o preco está sendo pedido, ele passa antes por GETTER E SETTER

p2 = Produto('Jordan', 'RS750')
p2.desconto(10)
print(p2.nome, p2.preco) # como o preco está sendo pedido, ele passa antes por GETTER E SETTER