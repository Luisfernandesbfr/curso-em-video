'''A Confederação Nacional de Natação precisa de um programa que
leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER'''
import datetime
atual = datetime.date.today().year
nas = int(input('Digite sua data de nascimento:'))
idade = atual - nas

if idade <= 9:
    print('Você tem {} anos e a sua categoria é a MIRIM'.format(idade))
elif idade > 9 and idade <= 14:
    print('Você tem {} anos e a sua categoria é a INFANTIL'.format(idade))
elif idade > 14 and idade <= 19:
    print('Você tem {} anos e a sua categoria é a JÚNIOR'.format(idade))
elif idade > 19 and idade <= 25:
    print('Você tem {} anos e a sua categoria é a SÊNIOR'.format(idade))
else:
    print('Você tem {} anos e a sua categoria é a MASTER'.format(idade))