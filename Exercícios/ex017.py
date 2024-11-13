'''Faça um programa que leia o comprimento do cateto oposto e do adjacente de um triângulo retângulo, calcule e mostre a hipotenusa.'''

import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}' .format(hi))

