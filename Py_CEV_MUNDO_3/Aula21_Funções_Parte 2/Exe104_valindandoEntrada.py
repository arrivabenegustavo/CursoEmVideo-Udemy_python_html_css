'''Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, 
só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)'''

def leiaint(num): # precisa receber com STRING para poder fazer a validação dentro da função
    ok = False # variável faz a validação para sair ou não do laço
    valor = 0 # variável para receber o valor de (n) convertido para (int)
    while True:
        n = input(num)
        if n.isnumeric(): # se for um número
            valor = int(n) # valor recebe e converte para (int)
            ok = True # passa a ser verdadeiro para sair do laço
        else:
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
        if ok: #sendo verdadeiro sai do laço
            break # está na ultima linha apenas, para poder retornar o valor após o break
                  # pois se o brek estivesse na linha 12 após ok ser verdadeiro, não conseguiria entrar corretamente na indentação
    return valor
               
#programa principal
n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}')