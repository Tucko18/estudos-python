n = input('digite algo: ')

print('você digitou um(a) {}'.format(type(n)))
print('Só tem espaços? {}'.format(n.isspace()))
print('É um número? {} '.format(n.isnumeric()))
print('É alfabético? {} '.format(n.isalpha()))
print('É alfanúmerico? {}'.format(n.isalnum()))
print('Está em letras maiusculas? {}'.format(n.isupper()))
print('Está em minúsculas? {}'.format(n.islower()))