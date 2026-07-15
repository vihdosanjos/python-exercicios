so = float(input('Qual é o salário antes do aumento? '))
sf = so + (so * 15 / 100)
print('Anteriormente, você ganhava R${}, com 15% de aumento, passará a receber R${:.2f}'.format(so, sf))
