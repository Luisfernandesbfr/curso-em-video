'''Faça um programa que leia o comprimento de três retas e diga ao usuario se elas
podem ou não ser um triângulo'''
print('-='*20)
print('Analisador de Triângulo')
print('-='*20)
r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))

if r1 < r2 + r3 and r2< r1 + r3 and r3 < r1 + r2:
    print(' Os segmentos acima podem formar triângulo')
else:
    print('Os segmentos acima não pode formar triângulo')