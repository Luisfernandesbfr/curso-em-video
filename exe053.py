'''Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e
quantas já são maiores.
'''
import datetime
atual = datetime.date.today().year
totmaior=0
totmenor=0
for c in range(1,8):
    nas = int(input('Em que ano a {} pessoa nasceu?'.format(c)))
    idade = atual - nas
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('Ao todo tivemos {} pessoas menores de idade'.format(totmenor))


