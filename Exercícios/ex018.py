#faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

'''Para expressões em graus, deverá efetuar a conversão de graus para radianos utilizando math.radians '''

import math
an = float(input("Digite o ângulo que deseja saber: "))
se = math.sin(math.radians(an))
print('O ângulo de {} tem o SENO de {:.2f}'.format(an, se))
co = math.cos(math.radians(an))
print('O ângulo de {} tem o COSSENO de {:.2f}' .format(an, co))
ta = math.tan(math.radians(an))
print('O ângulo de {} tem a TANGENTE de {:.2f}' .format(an, ta))