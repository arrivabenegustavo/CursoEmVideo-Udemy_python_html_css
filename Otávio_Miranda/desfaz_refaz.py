def cabecalho(txt):
    print('-' * 30) 
    print(txt.center(30))
    print('-' * 30) 
 
 
    
def mostra_lista(lista):
    cabecalho(f'TAREFAS:\n{lista}')   
# Função para remover tarefas da lista de tarefas e colocar na lista de armazenar
def desfaz(lista_tarefa, lista_armazena):
    if not lista_tarefa:
        cabecalho('Nada a desfazer!')
        return
    ultima_tarefa = lista_tarefa.pop()
    lista_armazena.append(ultima_tarefa)
        
# Função para devolver os tarefas para lista de tarefas, tarefas que estavam na lista de armazenar
def refaz(lista_tarefa, lista_armazena):
    if not lista_armazena:
        cabecalho('Nada a refazer!')
        return
    ultima_tarefa = lista_armazena.pop()
    lista_tarefa.append(ultima_tarefa)
    
    
def adiciona(lista_tarefa, tarefa):
    lista_tarefa.append(tarefa)
    
    

lista_tarefas = []
lista_armazena = [] # lista para armazenar os dados tirar ou devolver 

while True:
    tarefa = input('Digite uma tarefa ou desfazer, refazer, ls, sair : ')
    if tarefa == 'ls':
        mostra_lista(lista_tarefas)
        
    elif tarefa =='desfazer':
        desfaz(lista_tarefas, lista_armazena)
           
    elif tarefa == 'refazer':
        refaz(lista_tarefas, lista_armazena)
    
    elif tarefa == 'sair':
        break
    else:
        adiciona(lista_tarefas, tarefa)
        
        
   
        