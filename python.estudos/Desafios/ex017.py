import math

co = float(input('DIgite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa do triangulo de cateto oposto {} e cateto adjacente {} é igual a {}'.format(co, ca, hi))
