'''Escreva um programa que leia a velocidade de um carro
se ele ultrapassar os 80 km/h mostre uma mensagem dizendo que foi multado
a multa vai custar R$ 7,00 por cada km/h acima do limite'''

vel = int(input('Qual a velocidade do carro ? '))
mul = (vel - 80) * 7
if vel > 80:
    print('Você está acima da velocidade permitida de 80 km/h ')
    print('A sua multa será de {} reais'.format(mul))
else:
    print('Parabéns você está dentro da velocidade permitida')