lanche = ('hambúrguer','suco', 'pizza', 'pudim')
for comida in lanche:
    print(f'{comida}')

# Ou 
#Se necessário mostrar também a posição, melhor opção abaixo

#for c in range(0, len(lanche)): 
    #print(f'Vou  comer {lanche[c]} na posição {c}') # Para mostrar o que tem dentro da variável lanche na posição C > hambúrguer....pudim
    # se o print for apenas {c} mostrará a posição de cada palavra >0,1...3
    
#for pos, comida in enumerate(lanche):
    #print(f'Vou comer {comida} na posição {pos}') #pos de posição
