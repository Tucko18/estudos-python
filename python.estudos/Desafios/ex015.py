d = int(input('Por quanto dias o carro foi alugado: '))
km = float(input('QUantos km foram rodados durante os {} dias: '.format(d)))
v = (60 * d) + (km * 0.15)

print('O valor do carro após {} dias e {}km rodados é {} R$'.format( d, km, v))

