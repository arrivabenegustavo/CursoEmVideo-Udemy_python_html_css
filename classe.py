class Pessoa:
    def __init__(self, nome, comendo=False, falando=False):
        self.nome = nome
        self.comendo = comendo
        self.falando = falando
        
    
    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo')
            return
        
        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True
    
    def parar_comer(self):
        if self.comendo:
            self.comendo = False
            print(f'{self.nome} parou de comer')
            return
    
    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} está comendo e não pode falar.')
            return
        
        if self.falando:
            print(f'{self.nome} já está falando')
            return
        
        self.falando = True
        print(f'{self.nome} está falando: {assunto}')
        
        
# Código principal

p1 = Pessoa('Gustavo')

p1.comer('Hamburguer')
p1.parar_comer()
#p1.comer('maça')
p1.falar('èee campeãaooo!!!!')
p1.falar('Dalee tricolorr!!!')
            



