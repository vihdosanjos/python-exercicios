print('Hoje descobriremos a sua nota média baseada na nota das duas provas do semestre')

n1 = float(input('Qual foi a sua nota na primeira prova?: '))
n2 = float(input('Qual foi a sua nota na segunda prova?: '))
m = (n1 + n2)/2

#print('Sua média semestral será: {}'.format(m))
print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(n1, n2, m))
