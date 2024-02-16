import math
a = float(input('Digite o valor de um ângulo: '))
c = math.cos(a)
s = math.sin(a)
t = math.tan(a)

print('O ângulo {} tem como cosseno {:.3f} como seno {:.3f} e como tanjente {:.3f} '.format( a, c, s, t))

