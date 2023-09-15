'''Faça um programa que leia o ano de nascimento de um jovem e informe,
 de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
  se é a hora exata de se alistar ou se já passou do tempo do alistamento.
 Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''
import datetime
nas = int(input('Digite sua data de nascimento:'))
atual = datetime.date.today().year
idade = atual - nas
print('Quem nasceu em {} tem {} anos em {}'.format(nas,idade,atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE')
elif idade < 18:
    saldo = 18 - idade
    ano = nas + 18
    print('Ainda faltam {} anos para o seu alistamento' .format(saldo))
    print('Seu alistamento será em {}'.format(ano))
else:
    saldo = idade - 18
    ano = nas + 18
    print('Você ja deveria ter se alistado há {} anos'.format(saldo))
    print('Seu alistamento foi em {}'.format(ano))
