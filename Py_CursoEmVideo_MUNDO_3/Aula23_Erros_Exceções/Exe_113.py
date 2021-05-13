def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Por favor, digite um número inteiro válido.')
            continue
        else:
            return n

def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Por favor, digite um número real válido.') 
            continue
        else:
            return n
 
        
num =leiaint('Digite um valor: ')
num2 = leiafloat('Digite um número real: ')
print(f'O número inteiro digitado foi {num} e o real foi {num2}')        
        
        
        
        
        
    