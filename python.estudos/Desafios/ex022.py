nome = input('Digite seu nome completo: ').strip()
nn = nome.split()
n = len(nn[0])
j = nome.replace(' ', '')
print('''Seu nome completo em maiusculas é {} 
Seu nome em minusculas é {}
Seu nome tem {} letras
Seu primeiro nome tem {} letras'''.format(nome.upper(), nome.lower(), len(j), n))
