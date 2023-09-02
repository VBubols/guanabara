#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um trângulo retângulo, calcule o comprimento da hipotenusa
from math import hypot
cateto_oposto = float(input('Digite o valor do cateto oposto: '))
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))
print(f'A medida da hipotenusa é: {hypot(cateto_oposto, cateto_adjacente)}')