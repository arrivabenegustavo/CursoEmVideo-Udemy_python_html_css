import random
import string

# Gera um número inteiro entre (X, Y)
# inteiro = random.randint(10, 20)

# Gerar um número aleatório usando a função range()
inteiro = random.randrange(900, 1000, 10)

# Gera um número de ponto flutuante entra (X, Y)
# flutuante = random.uniform(10, 20)

# Gera um número de ponto flutuante entre 0 e 1
flutuante = random.random()

lista = ['Luiz', 'Otávio', 'Maria', 'Rose', 'Jenny', 'Danilo', 'Felipe']

# Seleciona aleatóriamente valores de uma lista
sorteio = random.sample(lista, 2) # nesse caso (2 valores)
# sorteio = random.choices(lista, k=2) # 2 valores
# sorteio = random.choice(lista) apenas 1 valor

# Embaralha a lista
random.shuffle(lista)

# Gera senha aleatória
letras = string.ascii_letters # letras maiúsculas e minúsculas
digitos = string.digits # Números
caracteres = '!@#$%&*._-'
geral = letras + digitos + caracteres
senha = "".join(random.choices(geral, k=20)) # 20 valores

print(senha)

