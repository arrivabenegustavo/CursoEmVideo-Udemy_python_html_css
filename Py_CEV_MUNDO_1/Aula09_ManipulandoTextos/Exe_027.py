nome = str(input('Digite seu nome completo: ')).strip()
nome = nome.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))
print('Total de Splits = {}'.format(len(nome)))

# a ultima linha usamos o "len" dentro dos colchetes para contar o total de splits
# que vai de 0 a x, sendo assim subtraindo do fim
# EX Gustavo = 0, Arrivabene = 1, de = 2, Abreu = 3..na contagem seriam 4  
# por ser 4 palavras que vai de 0 a 3, sendo 3 a ultima
# ao subtrair 4 - 1 da 3...mostrando assim a ultima palavra