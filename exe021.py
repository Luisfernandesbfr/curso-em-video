''' Crie um programa que leia o nome completo e mostre todas as letras
maiusculas, todas minusculas,quantas letras tem(sem o espaço) e quantas
 letras tem o primeiro nome'''

nome = input('Digite seu nome completo: ').strip()
print('Analisando seu nome ...')
print('Seu nome em maiusculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)- nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')) )
