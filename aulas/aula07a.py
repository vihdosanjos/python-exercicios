n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
a = n1 + n2
s = n1 - n2
m = n1 * n2
d = n1 / n2
p = n1 ** n2
di = n1 // n2
r = n1 % n2
print('A adição é {}, a subtração é {}, a multiplicação é {} e a divisão é {:.3f}'.format(a, s, m, d))
print('A potência é {}, a divisão inteira é {} e o resto é {}'.format(p, di, r))
