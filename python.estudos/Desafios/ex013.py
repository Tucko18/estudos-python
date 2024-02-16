s = float(input('Digite o salário atual do funcionario: '))
a = float(input('Digite quanto será seu aumento em %: '))
sf = s + (s * (a * 0.01))

print('O salário do funcionario após o aumento de {}% passará de {}R$ para {}R$'.format(a, s, sf))
