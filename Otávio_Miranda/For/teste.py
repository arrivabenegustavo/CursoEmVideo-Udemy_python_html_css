cpf = input('Digite seu CPF: ')
tot1 = tot2 = digito1 = digito2 = 0
mult = 1
for i, v in enumerate(cpf[-3::-1], 2):
    mult = i * int(v)
    tot1 += mult
result1 = 11 - (tot1 % 11)
if result1 < 9:
    digito1 = str(result1)
for i, v in enumerate(cpf[-2::-1], 2):
    mult = i * int(v)
    tot2 += mult 
result2 = 11 - (tot2 % 11)
digito2 = str(result2)

# evita validar números senquenciais como ex: 11111111111, 22222222222...etc
sequencia = cpf == str(cpf[0]) * len(cpf) 

if digito1 == cpf[-2] and digito2 == cpf[-1] and not sequencia:
    print('Cpf válido!')
else:
    print('Cpf inválido!')


