#crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
#import math #importa toda a biblíoteca math e como para esse exercício só foi utilizado a função trunc. Podemos importar apenas essa função. OBS.: Deve retirar a referência de math do código.

from math import trunc
num1 = float(input("Digite um número real, utilizando casas após a virgula: "))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num1, trunc(num1)))

#metodo trunc (trucate), onde ele irá cortar a parte inteira do número.

