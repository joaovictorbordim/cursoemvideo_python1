#Faça um algoritmo que leia o salário de um funciónario e mostre seu novo salário com 15% de aumento.

sal = float(input('Calculadora de reajuste de salário com 15% de aumento. \n\nDigite o salário atual: '))
por = sal * (15/100)
tot = sal + por
print('NOVO SALÁRIO: R${:.2f}'.format(tot))