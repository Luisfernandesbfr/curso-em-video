'''Desenvolva um programa que leia seis números inteiros e
mostre a soma apenas daqueles que forem pares. Se o valor
digitado for ímpar, desconsidere-o.
'''
soma = 0
for n in range(1,7):
    v = int(input('Digite um numero:'))
    if v % 2 == 0:
        soma = soma + v
print('A soma dos valores impares digitados é {}'.format(soma))