''' Elabore um programa que calcule o valor a ser pago por
 um produto, considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros'''
print('{:=^40}'.format(' LOJAS GUANABARA '))
preço = float(input('Preço das Compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão 
[ 4 ] 3x ou mais no cartão ''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 0.10)
elif opção == 2:
    total = preço - (preço * 0.05)
elif opção == 3:
    total = preço
    parcela = preço / 2
    print('Sua compra será parcelada em 2x de {}'.format(parcela))
elif opção == 4:
    total = preço * 1.20
    totp = int(input('Quantas parcelas? '))
    parcela = total / totp
    print('Sua Compra será parcelada em {} vezes de {:.2f} com juros'.format(totp,parcela))
else:
    total = 0
    print('Opção Invalida. TENTE NOVAMENTE')
print('Sua compra de R${} vai custar R${} no final'.format(preço,total))



