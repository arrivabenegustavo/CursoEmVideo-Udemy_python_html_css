frase = str(input('Digite uma frase: ')).strip().lower()
print('A letra "A" aparece {} vezes na frase.'.format(frase.count('a')))
print('A primeira letra "A" apareceu na posição {}'.format(frase.find('a')+1))
print('A última letra apareceu a posição {}'.format(frase.rfind('a')+1))


# rfind é usado para contar da direita para esquerda...assim mostrando a posição da ultima letra
# e o ( +1) é por conta do computador começar contando do zero, então se o a tiver na posição 0
# com + 1 ele mostrará posição 1, melhor visualização para o usuário