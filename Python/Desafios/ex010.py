#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
print('Cotação do dólar: R$4.88')
din = float(input('Quantos reais você tem? '))
conv = din/4.88
print(f'Você pode comprar aproximadamente {conv:.2f} dólares!')