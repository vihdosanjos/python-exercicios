l = float(input('Qual é a largura da sua parede em metros? '))
a = float(input('Qual é a altura da sua parede em metros? '))
ar = l * a
t = ar / 2
print('Para pintar essa parede de {:.2f}m², será necessário {:.2f}l de tinta'.format(ar, t))
