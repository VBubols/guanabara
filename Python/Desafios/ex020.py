#O mesmo progessor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o onome dos quatro alunos  e mostre a ordem sorteada
from random import sample
n1 = input('Nome do primeiro aluno: ')
n2 = input('Nome do segundo aluno: ')
n3 = input('Nome do terceiro aluno: ')
n4 = input('Nome do quarto aluno: ')
print(f'O aluno sorteado foi {sample([n1, n2, n3, n4], k=4)}')