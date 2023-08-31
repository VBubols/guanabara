#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessãrio para pintá-lo, sabendo que cada litro de tinta
#pinta uma área de 2m2
l = float(input('Quantos metros de largura tem a parede: '))
a = float(input('Quantos metros de altura tem a parede: '))
area = l*a
tinta = area/2
print(f'A parede tem {area}m2 e você vai precisar de {tinta} latas de tinta!')