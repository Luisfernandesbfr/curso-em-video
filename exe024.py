'''crie um programa e diga se ela tem "SILVA" no nome'''

nome = input('Digite seu nome completo: ').strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))
