'''Faça um programa que leia o comprimento do cateto oposto
e do cateto adjacente de um triangulo retangulo
calcule e mostre o comprimento da hipetenusa'''
import math

opo = float(input('Digite o comprimento do cateto oposto: '))
adj = float(input('Digite o comprimento do cateto adjacente: '))
hi = math.hypot(opo, adj)
print('A hipotenusa vai medir {:.2f}'.format(hi))
