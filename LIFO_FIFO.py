'''
Pilhas e Filas
LIFO (stack) -> Last in, First out
FIFO (queue) -> First in, First out
'''

# Para FIFO importamos o modulo COLLECTIONS(deque)
# deque -> é um tipo de lista
# Tudo dentro de COLLECTIONS são estrutura de dados de alto desempenho
# Usado para quando usar muitos dados

from collections import deque
from time import sleep
'''fila = deque()
fila.append('chegou 1')
fila.append('chegou 2')
fila.append('chegou 3')
fila.append('chegou 4')
fila.popleft() #exclui sempre o primeiro
print(fila)'''

fila = deque(maxlen=5)
# neste caso, sempre que for informado mais de cindo dados, ele removerá o primeiro dado automaticamente
# Exemplo:

for i in range(25):
    fila.append(i)
    sleep(1)
    print(fila)


