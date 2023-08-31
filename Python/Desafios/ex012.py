#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
pre = float(input('Qual o preço do produto? '))
desc = pre*5/100
print(f'O desconto será de R${desc:.2f}')
novo_pre = pre-desc
print(f'O produto custará R${novo_pre:.2f}')