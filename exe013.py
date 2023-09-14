# aluguel de carros. a quantidade de km e a quantidade de dias sabendo que o dia custa R$60 e o km R$ 0,15

d=int(input('Quantos dias você alugou o carro ? '))
k=float(input('Quantos KMs você andou com o carro ? '))
t= (d * 60) + (k*0.15)
print('Voce alugou o carro por {} dias e andou {:.2f} Kms, você tera que pagar R$ {:.2f} '.format(d,k,t))