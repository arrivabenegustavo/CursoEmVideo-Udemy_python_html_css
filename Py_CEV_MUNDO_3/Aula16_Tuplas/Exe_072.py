# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
contagem = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez')
while True:
    n = int(input('Digite um número entre 0 e 10: '))
    if 0 <= n <= 10:
        print(f'Você digitou o número {contagem[n]}')    
        resp = ' '                   
        while resp not in 'SN': 
            resp = str(input('Quer continuar: ')).strip().upper()[0]
        if resp == 'N':
            break           
print('\nPrograma finalizado, obrigado!\n') 

        # como N recebe um número inteiro e a tuplas está nomedada de zero a 10
        # basta colocar o N para mostrar, pois se digitado 3 aparecerá o que estiver na posição 3
        # que neste caso é 'Três'