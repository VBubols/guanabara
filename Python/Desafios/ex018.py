#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
from math import cos, sin , tan, ceil, radians, floor
x = float(input('Digite um ângulo: '))
seno = sin(x)
cosseno = cos(x)
tangente = tan(x)
print(f'Valor do cosseno: {ceil(cosseno)} \nValor do seno: {floor(seno)} \nValor da tangente: {ceil(tangente)}')
