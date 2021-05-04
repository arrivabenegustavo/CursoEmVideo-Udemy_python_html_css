r1 = float(input("Digite a primeira reta: "))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))

# Para formar um triângulo, a MAIOR reta deve ser MENOR do que a SOMA das outras duas retas
# Ou se tiverem o mesmo tamanho, tbm podem formar um triângulo.

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas a cima PODEM FORMAR UM TRIÂNGULO')
else:
    print('As retas acima NÃO PODEM FORMAR UM TRIÂNGULO') 
