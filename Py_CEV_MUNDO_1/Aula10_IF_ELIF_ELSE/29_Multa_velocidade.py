veloc = int(input('Qual a velocidade Km/h vc passou: '))
if veloc > 80:
    limite = veloc - 80 # valor excedente 
    multa = limite * 7 # valor da multa R$
    print('MULTADO!! Você excedeu o limite de velocidade que é 80km/h')
    print('Sendo {}km/h acima do limite de velocidade \nSua multa foi de R$ {:.2f}\n'.format(limite, multa))   
else:
    print('Você está dentro do limite de velocidade(80km/h)\n')
print('Tenha um bom dia! Dirija com segurança') # aparece independentemente da condição    