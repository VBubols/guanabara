#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
salario = float(input('Qual seu salário? R$'))
aumento = salario*15/100
print(f'Seu aumento será de R${aumento:.2f}')
novo_salario = salario+aumento
print(f'Seu novo salário será de R${novo_salario:.2f}')