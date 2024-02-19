nome = str(input('Qual seu nome completo: ')).split()
n = ('-').join(nome)
v = n.find('-')
j = (n.rfind('-')) + 1
pn = n[:v]
un = n[j:]
print('Prazer em te conhecer !')
print('Seu primeiro nome é', pn)
print('Seu último nome é', un)


