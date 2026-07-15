print('Conversor de metros')
n = float(input('Metros: '))
k = n/1000
h = n/100
d = n/10
dm = n*10
c = n*100
m = n*1000
print('A medida de {}m corresponde a \n{}km \n{:.3f}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(n, k, h , d, dm, c, m))

