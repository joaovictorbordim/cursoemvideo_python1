#Crie um algoritmo que leia um número e mostre o seu dobro, tripo e raiz quadrada

n1 = int(input('Cálculo de dobro e tripo. Digite um número inteiro: '))
do = n1 * 2
tr = n1 * 3
ra = n1 ** (1/2)

print('O dobro é {} e o tripo {} do número digitado {} e sua raiz quadra é {:.2f}.' .format(do, tr, n1, ra))
