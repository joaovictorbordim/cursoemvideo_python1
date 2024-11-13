#Desenvolva um programa que leia as duas notas de um aluno e calcule e mostre a média.

n1 = int(input('Cálculo de média de notas! Digite a primeira : '))
n2 = int(input('Digite a segunda nota: '))
n3 = int(input('Digite a terceira nota: '))
so = n1 + n2 + n3
me = so / 3

print('A somatória das nota é {} e sua média é: {:.1f}'.format(so, me))