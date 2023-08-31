#Criar um programa que leia um valor e uma porcentagem e calcule tudo
valor = float(input('Digite o valor: '))
porcentagem = float(input('Digite a porcentagem: '))
print(f'O valor escolhido foi {valor} e a porcentagem foi {porcentagem}%')

porcentagem = valor*porcentagem/100

resposta = int(input('Digite 1 se for uma soma ou 2 para subtração '))

if resposta==1:  
    valor = valor+porcentagem
    print(f'O novo valor será: {valor}')
elif resposta==2:
    valor = valor-porcentagem
    print(f'O novo valor será: {valor}')
else:
    print('Valor inválido')