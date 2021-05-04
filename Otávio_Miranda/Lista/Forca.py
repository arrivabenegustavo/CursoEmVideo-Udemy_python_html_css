'''Faça um jogo da forca em que o usuário digitará uma de letra até acertar a palavra secreta
ele terá uma quantidade DETERMINADA DE CHANCES e mostre a quantidade de tentativas erradas.'''

secreta = 'JORDAN'
digitada = []
chances = 3
print('*'*24)
print(f'{"ADIVINHE A PALAvRA": ^24}')
print('*'*24)
print('VOCÊ TERÁ 3 CHANCES DE ERRO!')
print(f'A Palavra tem {len(secreta)} letras.\nBOA SORTE!')
print('-'*30)
while True:
    letra = input('Digite uma letra: ').strip().upper()
    print()
    if len(letra) > 1:
        print('Maaah tu é burro é??? UMA LETRAAA!!')
        continue
    if letra in secreta:
        digitada.append(letra)
        print(f'Booaaa, a letra "{letra}" FAZ parte da palavra\n')
    else:
        print(f'Putzz, a letra "{letra}" NÃO FAZ parte da palavra\n')
        chances -= 1 
    if chances > 0:
        print(f'Você ainda tem {chances} chances de erro!')
        print('-'*33)   
    else:
        print('VOCÊ PERDEU!!')
        print(f'A palavra é {secreta}')
        break     
    # este laço FOR vereifica se letras DIGITADAS contem algum letra da palavra SECRETA
    # se existir, a nova palavra recebe a LETRA CERTA e acrescenta '*' para completar o resto da palavra
    # pois este laço gira até a quantidade da palavra secreta.
    secreta_digitada = ''
    for letra_certa in secreta:
        if letra_certa in digitada:
            secreta_digitada += letra_certa
        else:
            secreta_digitada += '*' 
    print(f'{secreta_digitada: ^30}')
    print('-'*33)
    if len(digitada) == len(secreta_digitada):
        print('VOCÊ VENCEU!\nCONGRATULATIONS!!!\n')
        break    