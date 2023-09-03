#Um progessor que sortear um dos seus quatro alunos para apgar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
from random import choice
n1 = input('Nome do primeiro aluno: ')
n2 = input('Nome do segundo aluno: ')
n3 = input('Nome do terceiro aluno: ')
n4 = input('Nome do quarto aluno: ')
print(f'O aluno sorteado foi {choice([n1, n2, n3, n4])}')