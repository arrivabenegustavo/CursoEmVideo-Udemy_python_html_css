cidade = ['sao paulo','belo horizonte','salvador','monte belo', 'carapicuiba']

estado = ['SP','MG','BA']

#ZIP
#cidade_estado = zip(cidade, estado)
#cidade_estado = zip(estado, cidade) #invertido
#print(list(cidade_estado))


#ZIP_LONGEST
from itertools import zip_longest
# os valores não existentes da lista menor mostrará ESTADO
cidade_estado = zip_longest(estado, cidade, fillvalue='Estado')
for valor in cidade_estado:
    print(valor)