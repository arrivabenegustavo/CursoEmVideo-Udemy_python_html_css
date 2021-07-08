sal = float(input('Qual é o salário do funcionário: '))
if sal <= 1250:
    novo = sal + (sal * 15 / 100)
    print('Funcionário ganhava R${:.2f} e passou a ganhar R${:.2f}.'.format(sal,novo))
else:
    novo = sal + (sal * 10 / 100)
    print('Funcionário ganhava R${:.2f} e passou a ganhar R${:.2f}.'.format(sal,novo))