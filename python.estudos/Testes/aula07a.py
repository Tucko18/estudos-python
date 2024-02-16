n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
p = n1 ** n2
div = n1 // n2
res = n1 % n2
sub = n1 - n2


print(' A soma vale {} \n a subtração vale {} \n a multiplicação vale {} \n a divisão vale {:.3f} \n o resto da'
      ' divisão é {} \n a divisão inteira vale {} \n a potenciação vale {} '.format(s, sub, m, d, res, div, p))
