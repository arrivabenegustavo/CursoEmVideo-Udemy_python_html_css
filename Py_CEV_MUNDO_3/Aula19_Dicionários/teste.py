lista = list()
times = dict()
for c in range (0, 3):
    times['nome'] = input('Nome: ')
    times['apelido'] = input('Apelido: ')
    times['estadio'] = input('Estádio: ')
    lista.append(times.copy())
for t in lista:
    for k, v in t.items():
        print(f'O {k} é {v}')
    
    