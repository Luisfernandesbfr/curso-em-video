'''faça um programa que leia um angulo e mostre na tela o valor do seno
cosseno e tangente do angulo'''

import math
ang = float(input('Digite um ângulo: '))
seno = math.sin(math.radians(ang))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang,seno))
cos = math.cos(math.radians(ang))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang,cos))
tan = math.tan((math.radians(ang)))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ang,tan))