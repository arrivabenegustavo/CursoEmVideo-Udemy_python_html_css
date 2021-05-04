larg = float(input('Digite a altura: '))
alt = float(input('Digite a largura: '))
area = larg * alt
tinta = area / 2
print('Sua parede te a dimensão de {}x{} e sua área é de {}m2'.format(larg,alt,area))
print('Será necessário {}L de tinta para pintura desta parede'.format(tinta))
