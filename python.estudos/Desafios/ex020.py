import random


n1 = input('Primeiro nome: ')
n2 = input('Segundo nome: ')
n3 = input('Terceiro nome: ')
n4 = input('Quarto nome: ')
lista = [n1, n2, n4, n3]
random.shuffle(lista)
print('A ordem de apresentação será \n{}'.format(lista))
