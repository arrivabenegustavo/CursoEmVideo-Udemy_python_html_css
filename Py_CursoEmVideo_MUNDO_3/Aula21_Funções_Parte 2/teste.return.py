def fatorial(n = 1):
    f = 1
    for c in range(n , 0, -1):
        f *= c
    return f
fat = int(input('Digite um número para ver o resultado: '))
print(fatorial(fat))