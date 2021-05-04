km = int(input('Quantos km rodou: '))
dias = int(input("Quantas diárias: "))
apagar = (km * 0.15) + (dias * 60)
print("O valor total a pagar é R${:.2f}".format(apagar))