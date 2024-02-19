frase = input('Digite uma frase: ' ).upper()
v = frase.count('A')
p = frase.find('A') + 1
u = frase.rfind('A') + 1
print('A letra A aparece {} vezes na frase'.format(v))
print('A letra A aparece pela primeira vez na posição {} '.format(p))
print('A letra A aparece pela última vez na posição {} '.format(u))
