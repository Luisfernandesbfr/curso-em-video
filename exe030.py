'''Desenvolva um program que pergunte a distancia de uma viagem em km
calcule o preço da passagem cobrando R$0.50 por km para viagens de ate 200 km
e R$0.45 para viagens mais longas'''

via = float(input('Qual a distancia da sua viagem ? KM'))
cur = via * 0.50
lon = via * 0.45
if via <= 200:
    print('Sua viagem custara {} Reais '.format(cur))
else:
    print('Sua viagem custara {} Reais '.format(lon))
