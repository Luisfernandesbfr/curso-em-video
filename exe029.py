'''crie um programa que leia um numero inteiro e mostre na tela se é par ou impar'''
num = int(input('Digite um numero: '))
resultado = num % 2
if resultado == 0:
    print('O  número {} é par'.format(num))
else:
    print('O numero {} é impar'.format(num))
