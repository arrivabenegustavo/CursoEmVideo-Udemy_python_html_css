'''
AGREGAÇÃO -> As classes podem existir sozinhas mas uma depende da outra para funcionar
'''


class CarrinhoCompras:
    def __init__(self):
        self.produtos = []
        
    def inserir(self, produto):
        self.produtos.append(produto)
        
    def listar(self):
        for produto in self.produtos:
            print(produto.nome, produto.preco)
    def soma(self):
        total = 0
        for produto in self.produtos:
            total += produto.preco
        return total
        
class Produtos:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
carrinho = CarrinhoCompras()

p1 = Produtos('Jordan', 750)
carrinho.inserir(p1)
p2 = Produtos('Camisa', 100)
carrinho.inserir(p2)
carrinho.listar()
print(f'Total de {carrinho.soma()}')

   
   