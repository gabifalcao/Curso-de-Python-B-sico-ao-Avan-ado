#f-strings
nome = 'Gabi'
idade = 20
hobbie = 'desenhar'
reais = 5000

linha1 = f'Oi eu sou a {nome} e tenho {idade} anos'
linha2 = f'Eu gosto de {hobbie}'
linha3 = f'Tenho {reais:,.3f} no banco'

print(linha1)
print(linha2)
print(linha3)

#método format
a = 'AA'
b = 'BB'
c = 1.5

teste = 'a = {} b = {} e c = {:.2f}'.format(a , b ,c )
print(teste)

teste2 = 'a = {0} a = {0} a = {0} b = {1} e c = {2:.2f}'.format(a , b ,c )
print(teste2)

#parametro nomeado 
d = 'DD'
e = 'EE'
f = c * 2

teste3 = ' d = {nome1} e = {nome2} e f ={nome3}'.format(nome1 = d , nome2 = e , nome3 = f)
print(teste3)