'''Escreva um programa para aprovar o empréstimo
bancário para a compra de uma casa. Pergunte o valor da casa,
o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário
ou então o empréstimo será negado.'''

casa = float(input('Qual o valor da casa ? R$ '))
sal = float(input('Qual é o seu salario ? R$ '))
pres = int(input('Em quantas prestações você irá pagar ? '))
vpres = casa / pres
minimo = sal * 0.30
print('Para pagar uma casa de R$ {:.2f} em {} prestações, seu valor mensal sera de R$ {:.2f}'.format(casa,pres,vpres))
if vpres <= minimo:
    print('Empréstimo CONCEDIDO !')
else:
    print('Empréstimo NEGADO !')
