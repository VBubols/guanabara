#Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
#Calcule o preço a pagar, sabendo que o ocarro custa R$60 por dia e R$0.15 por KM rodado
dias = int(input('Quantos dias você ficou com o carro? '))
km = float(input('Quantos KM foram percorridos? '))
preco = (dias * 60) + (km * 0.15)
print(f'O total a pagar será: R${preco:.2f}')