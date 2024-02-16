v = float(input('Digite o valor de um produto com desconto: '))
d = float(input('Digite quantos % de desconto tem esse produto: '))
vf = v - (v * (d * 0.01))


print('O produto de {}R$ com {}% de desconto é igual a {} '.format(v, d, vf))

