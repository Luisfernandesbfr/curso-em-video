'''Faça um programa que pergunte o salario e calcule o valor do aumento
para salarios superiores a R$1250 calcule um aumento de 10%
para os inferiores 15%'''

sal = float(input('Qual é o seu salario ? '))
if sal > 1250:
    nsal = sal * 1.10
else:
    nsal = sal * 1.15

print(' Seu novo salario é {:.2f} Reais '.format(nsal))