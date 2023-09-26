'''Refaça o DESAFIO 11, mostrando a tabuada de um número
 que o usuário escolher, só que agora utilizando um laço for.'''
num = int(input('Digite um numero para ver sua tabela:'))
for t in range(1,11):
    print('{} x {:2} = {}'.format(num, t, num * t))