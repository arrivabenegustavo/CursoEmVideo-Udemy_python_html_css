def teste(b):
    global a
    a = 4
    b += 10
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
#programa principal
a = 8
teste(a)
print(f'A fora vale {a}')
