#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
m = float(input('Escreve um valor em metros: '))
km = m*1000
hm = m*100
dam = m*10
dm = m/10
cm = m/100
mm = m/1000
print(f'Valor em metros: {m}')
print(f'Valor em quilomêtros: {km}')
print(f'Valor em hectômetro: {hm}')
print(f'Valor em decâmetro: {dam}')
print(f'Valor em decímetro: {dm}')
print(f'Valor em centímetro: {cm}')
print(f'Valor em milìmetro: {mm}')