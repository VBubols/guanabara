n = input('Digite algo:')
print(f'Você digitou: {n}')
print(f'O tipo primitivo desse valor é:{type(n)}')
print('É numérico:', n.isnumeric())
print('É alfabético:', n.isalpha())
print('É alfanumérico:', n.isalnum())
print('É um identificador:', n.isidentifier())
print('Está em minusculo:', n.islower())
print('Está em maisculo:', n.isupper())
print('Está capitalizada:', n.istitle())
print('Contém só espaços', n.isspace())