# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
lista = []
expressao = str(input('Digite uma expressão: '))
for parentese in expressao:
    if parentese == '(':
        lista.append(parentese)
    elif parentese == ')':
        lista.pop()
if len(lista) == 0:   
    print('\nSua expressão está válida\n')
else:
    print('\nSua expressão não é valida\n')
            
            