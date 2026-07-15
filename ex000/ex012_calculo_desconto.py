o = float(input('Qual é o valor do produto origionalmente? R$' ))
f = o - (o * 5/100)
print('O preço final do produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(o, f))
