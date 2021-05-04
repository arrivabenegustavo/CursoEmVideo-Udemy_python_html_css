n = [3,2,6,7,1]
n.append(8) #inclui o 8 no final
n.insert(2,4) # insere o 4 na posição 2, fazendo com que os números da frente mudem de posição tbm
del n [1] # remove a posição 1
n.pop(1) # IDEM a cima
n.pop() # remove a ultima posição
n.remove(6) # Remove pelo conteúdo da posição. Vai procurar onde está o 3 e remover
#obs: se houver dois ou mais números iguais, eliminara o primeiro, pois ele não varre a lista inteira
#para remover mais de um número igual, basta usar um laço 
n.sort() # Coloca na ordem CRESCENTE
n.sort(reverse=True) # Coloca em ordem DECRESCENTE
print(n)
