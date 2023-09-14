#faça um programa que pegue o valor e de 5% de desconto
p=float(input('Qual o valor: '))
n= p - (p*0.05)
print('O produto custava {:.2f} e agora com o desconto o valor é {:.2f} Reais'.format(p,n))