d = int(input('O carro foi alugado por quantos dias? '))
km = float(input('Quantos km foram rodados? '))
total = (d * 60) + (km * 0.15)
print('O total a pagar será de R${:.2f}'.format(total))
