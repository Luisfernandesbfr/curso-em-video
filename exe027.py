'''Faça um programa em que o computador escolha um numero inteiro entre 0 e 5
e peça para o usuario tentar descobrir qual foi o numero escolhido o programa
devera escrever na tela se o usuario venceu ou perdeu'''
import random
import time
computador = random.randint(0,5)
print('-=-' * 20 )
print('Vou pensar em um numero entre 0 e 5 . Tente advinhar...' )
print('-=-' * 20 )
jogador = int(input('Em que numero eu pensei ? '))
print('PROCESSANDO...')
time.sleep(2)
if jogador == computador:
    print('Parabens você venceu')
else:
    print('GANHEI, eu pensei no numero {} e não no {}'.format(computador,jogador))