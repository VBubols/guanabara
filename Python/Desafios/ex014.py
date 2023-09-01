#Escreva um programa que converta uma temperatua digita em °C 
#e converta para °F
c = float(input('Digite a temperatura em Celsius: '))
f = float((c * 9 / 5) + 32)
print(f'A temperetura em Fahrenheit é: {f:.2f} °F')
