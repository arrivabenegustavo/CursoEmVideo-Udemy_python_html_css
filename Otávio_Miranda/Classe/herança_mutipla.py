from log import LogMixin

class Eletronico:
    def __init__(self, nome):
        self.nome = nome 
        self.ligado = False
    
    def ligar(self):
        if self.ligado:
            print(f'{self.nome} já está ligado')
            return
        self.ligado = True
        print(f'{self.nome} foi ligado')
        
    def desligar(self):
        if not self.ligado:
            print(f'{self.nome} já está desligado')
            return
        self.ligado = False
        print(f'{self.nome} foi desligado')
        
class Celular(Eletronico, LogMixin): # Herança múltipla, executa da esquerda para direita
    def __init__(self, nome):
        super().__init__(nome)
        self.conectado = False
        
    def conectar(self):
        if not self.ligado:
            error = f'{self.nome} está desligado e não pode conectar'
            print(error)
            self.log_error(error) # método dentro de LogMixin
            return
        
        if self.conectado:
            error = f'{self.nome} já está conectado'
            print(error)
            self.log_error(error)
            return
        
        self.conectado = True
        info = f'{self.nome} Conectado' 
        print(info)
        self.log_info(info) # método dentro de LogMixin   
                
        
    def desconectar(self):
        if not self.conectado:
            error = f'{self.nome} já está desconectado'
            print(error)
            self.log_error(error)
            return
        
        self.conectado = False
        info = f'{self.nome} foi desconectado'
        print(info)
        self.log_info(info)
        
        
celular = Celular('Iphone')
celular.conectar() 
celular.desconectar() 
celular.ligar()
celular.conectar() 
celular.conectar() 
celular.conectar() 
 
