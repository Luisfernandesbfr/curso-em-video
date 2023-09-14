'''crie um programa que leia um nome de uma cidade
e dia se ela começa ou não com SANTO'''

cid = input('Em que cidade você nasceu ?  ').strip()
print(cid[:5].upper() == 'SANTO' )