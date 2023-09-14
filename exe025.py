'''crie um programa que leia uma frase e diga
quantas vezes aparece a letra A
em que posiçao ela aparece a primeira vez
em que posiçaõ aparece a ultima vez'''

fra =str( input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes'.format(fra.count('A')))
print('A primeira letra A apareceu na posiçao {}'.format(fra.find('A')))
print('A ultima letra A apareceu na posiçao {}'.format(fra.rfind('A')))