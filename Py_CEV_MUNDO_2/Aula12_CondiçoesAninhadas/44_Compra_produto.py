'''Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
à vista dinheiro/cheque: 10% de desconto
à vista no cartão: 5% de desconto
em até 2x no cartão: preço formal 
3x ou mais no cartão: 20% de juros'''
preço = float(input('Valor das compras: '))
print('''Escolha a forma de pagamento:
[1] À vista dinheiro/cheque \033[1;32mDESCONTO de (10%)\033[m.
[2] À vista no cartão \033[1;32mDESCONTO de (5%)\033[m.
[3] 2x no cartão \033[1;33mSEM DESCONTO\033[m.
[4] 3x ou mais no cartão \033[1;31mACRÉSCIMO de (20%)juros\033[m.''')
pgto = int(input('Digite a opção desejada: '))
if pgto == 1:
    novopreço = preço - (preço * 10 / 100) #desconto de 10%
elif pgto == 2:
    novopreço = preço - (preço * 5 / 100) #desconto de 5%
elif pgto == 3:
    novopreço = preço
    parcela = preço / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM DESCONTO'.format(parcela))
elif pgto == 4:
    qntd = int(input('Quantas parcelas deseja? '))
    novopreço = preço + (preço * 20 / 100) #Acréscimo de 20%
    parcela = novopreço / qntd #Valor da parcelas R$
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(qntd, parcela))
else:
    print('Opção inválida. Tente novamente!')
print('Valor das compras R${:.2f}\nValor a ser pago R${:.2f}'.format(preço, novopreço)) 
''' este ultimo print mostra o resultado de todas as opções escolhidas
pois ele está fora dos "IFS"'''