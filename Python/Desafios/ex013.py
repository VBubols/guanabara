#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
salario = float(input('Qual seu salário? '))
porcentagem = 15*salario
aumento = porcentagem/100
novo_salario = aumento+salario
print(f'Seu novo salário será de R${novo_salario}')