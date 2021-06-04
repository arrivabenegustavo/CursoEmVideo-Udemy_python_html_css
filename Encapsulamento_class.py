'''
public -> atributo publico (consegue acessar ou modificar fora da classe)
_ protected -> '_' antes do atributo, sugere que não seja acessado ou modificado fora da classe 
__ private -> '__' antes do atributo, sugere com mais veemencia que não seja acessado ou modificado fora da classe
'''



class BaseDeDados:
    def __init__(self):
        self._dados = {}

    def inserir(self, id, nome):
        if 'Clientes' not in self._dados:
            self._dados['Clientes'] = {id: nome}
        else:
            self._dados['Clientes'].update({id: nome})
            
    def listar(self):
        for id, nome in self._dados['Clientes'].items():
            print(id, nome)
            
    def deletar(self, id):
        del self._dados['Clientes'][id]
            
bd = BaseDeDados()
bd.inserir(1, 'Gustavo')
bd.inserir(2, 'Thais')
bd.inserir(3, 'Jordan')
#print(bd.dados)
bd.listar()
print('Após remoção de um cliente')
bd.deletar(3)
bd.listar()
