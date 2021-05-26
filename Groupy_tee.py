from itertools import groupby, tee

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'C'},
    {'nome': 'Anderson', 'nota': 'B'},
]

#função para usar a chave NOTA
def ordena(item):
  return item['nota']

# coloca as notas em ordem alfabética
alunos.sort(key=ordena)
# Agrupa as notas iguais
alunos_agrupados = groupby(alunos, ordena)

'''
# Sem tee (com list)
for agrupamento, valores_agrupados in alunos_agrupados:
  valores = list(valores_agrupados)
  print(f'Agrupamento: {agrupamento}')
  for aluno in valores:
    print(f'\t{aluno}')
  quantidade = len(valores)
  print(f'\t{quantidade} alunos tiraram nota {agrupamento}')
'''

# Com tee
for agrupamento, valores_agrupados in alunos_agrupados:
# função TEE para copiar os VALORES_AGRUPADOS nas variaveis VA1 e VA2
# Por VALORES_AGRUPADOS ser um iterador, os valores foram esgotados
# e por isso foi necessário a copia em outras variáveis.
  v1, v2 = tee(valores_agrupados)

  print(f'Agrupamento: {agrupamento}')

  for aluno in v1: # Variável que foi copiada
    print(f'\t{aluno}')
    
# VA1 esgotou os valores e usamos a segunda variável copiada VA2
  quantidade = len(list(v2))
  print(f'\t{quantidade} alunos tiraram nota {agrupamento}')